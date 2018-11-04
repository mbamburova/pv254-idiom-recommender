import {IQuestion} from '../../models/Question';
import {Action} from '../../models/Action';
import {Question_Generated} from '../../actions/actionTypes';

export const currentQuestion = (state: IQuestion | null = null, action: Action): IQuestion | null => {
  switch (action.type) {
    case Question_Generated:
      return action.payload.question;

    default:
      return state;
  }
};
