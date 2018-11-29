import {CurrentUserServerModel} from '../serverModels/CurrentUserServerModel';
import {QuestionServerModel} from '../serverModels/QuestionServerModel';
import {CorrectnessServerModel} from '../serverModels/CorrectnessServerModel';

export interface IQuestionRepository {
  getQuestion: (currentUser: CurrentUserServerModel) => Promise<QuestionServerModel>;
  answerQuestion: (currentUser: CurrentUserServerModel, questionId: number, answerId: number) => Promise<CorrectnessServerModel>;
}
