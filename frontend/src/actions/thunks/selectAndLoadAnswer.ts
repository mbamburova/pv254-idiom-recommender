import {answerSelected, correctAnswerLoaded} from '../appActions';
import {Dispatch} from 'redux';
import {IQuestionRepository} from '../../repositories/interfaces/IQuestionRepository';
import {createGenerateQuestionAction} from './generateQuestion';
import {IUser} from '../../models/User';

const waitingTimeMs = 1000;

export async function createSelectAndLoadAnswerAction(questionRepository: IQuestionRepository, currentUser: IUser, questionId: string, selectedAnswerId: string, dispatch: Dispatch) {
  dispatch(answerSelected(selectedAnswerId));
  const correctness = await questionRepository.answerQuestion(questionId, selectedAnswerId);
  dispatch(correctAnswerLoaded(correctness.correct_answer_id));
  await new Promise(resolve => setTimeout(resolve, waitingTimeMs));
  await createGenerateQuestionAction(questionRepository, currentUser, dispatch);
}
