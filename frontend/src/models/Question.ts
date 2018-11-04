import {getAnswerFromServerModel, IAnswer} from './Answer';
import {List} from 'immutable';
import {QuestionServerModel} from '../repositories/serverModels/QuestionServerModel';
import {AnswerServerModel} from '../repositories/serverModels/AnswerServerModel';

export interface IQuestion {
  readonly question: string;
  readonly id: string;
  readonly answers: List<IAnswer>;
  readonly type: number;
}

export function getQuestionFromServerModel(serverModel: QuestionServerModel): IQuestion {
  return {
    question: serverModel.question,
    id: serverModel.question_id,
    type: serverModel.question_type,
    answers: List(serverModel.answers.map((answer: AnswerServerModel) => getAnswerFromServerModel(answer)))
  };
}
