import {Action} from '../../models/Action';
import {Question_Answer_Selected, Question_Generated} from '../../actions/actionTypes';

export const selectedAnswerId = (state: number | null = null, action: Action): number | null => {
  switch (action.type) {
    case Question_Generated:
      return null;

    case Question_Answer_Selected:
      return action.payload.answerId;

    default:
      return state;
  }
};
