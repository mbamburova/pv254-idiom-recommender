import {SERVER_BASE_URL} from './constants';
import {QuestionServerModel} from './serverModels/QuestionServerModel';
import {IQuestionRepository} from './interfaces/IQuestionRepository';
import {CorrectnessServerModel} from './serverModels/CorrectnessServerModel';
import {CurrentUserServerModel} from './serverModels/CurrentUserServerModel';

export const questionRepository: IQuestionRepository = {
  getQuestion: (currentUser: CurrentUserServerModel): Promise<QuestionServerModel> => {
    return fetch(`${SERVER_BASE_URL}/question/${currentUser.id}`)
      .then(response => {
        if (!response.ok) {
          throw new Error(response.statusText);
        }
        return response.json();
      });
  },
  answerQuestion: (currentUser: CurrentUserServerModel, questionId: number, answerId: number): Promise<CorrectnessServerModel> => {
    return fetch(`${SERVER_BASE_URL}/answer/${currentUser.id}/${questionId}/${answerId}'`)
      .then(response => {
        if (!response.ok) {
          throw new Error(response.statusText);
        }
        return response.json();
      });
  },
};
