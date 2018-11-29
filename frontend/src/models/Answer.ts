import {AnswerServerModel} from '../repositories/serverModels/AnswerServerModel';

export type IAnswer = {
  readonly id: number;
  readonly text: string;
};

export function getAnswerFromServerModel(serverModel: AnswerServerModel): IAnswer {
  return {
    id: serverModel.answer_id,
    text: serverModel.answer_text,
  };
}
