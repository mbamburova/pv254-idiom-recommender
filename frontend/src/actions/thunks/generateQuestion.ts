import {Dispatch} from 'redux';
import {IUser, userToServerModel} from '../../models/User';
import {questionGenerated} from '../appActions';
import {IQuestionRepository} from '../../repositories/interfaces/IQuestionRepository';
import {QuestionServerModel} from '../../repositories/serverModels/QuestionServerModel';
import {getQuestionFromServerModel} from '../../models/Question';

export function createGenerateQuestionAction(questionRepository: IQuestionRepository, currentUser: IUser | null, dispatch: Dispatch) {
  if (currentUser === null) {
    return Promise.resolve();
  }

  return questionRepository.getQuestion(userToServerModel(currentUser))
    .then((serverQuestion: QuestionServerModel) => {
      const question = getQuestionFromServerModel(serverQuestion);
      dispatch(questionGenerated(question));
    });
}
