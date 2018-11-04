import {Action} from '../../models/Action';
import {Question_Correct_Answer_Loaded, Question_Generated} from '../../actions/actionTypes';

export const correctAnswerId = (state: string | null = null, action: Action): string | null => {
  switch (action.type) {
    case Question_Generated:
      return null;

    case Question_Correct_Answer_Loaded:
      return action.payload.answerId;

    default:
      return state;
  }
};
