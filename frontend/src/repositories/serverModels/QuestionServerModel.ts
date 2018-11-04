import {AnswerServerModel} from './AnswerServerModel';

export interface QuestionServerModel {
  readonly question: string;
  readonly question_id: string;
  readonly answers: AnswerServerModel[];
  readonly question_type: number;
}
