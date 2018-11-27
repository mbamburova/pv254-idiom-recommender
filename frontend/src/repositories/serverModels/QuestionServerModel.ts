import {AnswerServerModel} from './AnswerServerModel';

export interface QuestionServerModel {
  readonly question: string;
  readonly question_id: number;
  readonly answers: AnswerServerModel[];
}
