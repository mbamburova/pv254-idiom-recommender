import {Action} from '../../models/Action';
import {User_PassedIntroduction} from '../../actions/actionTypes';

export const hasUserPassedIntroduction = (state: boolean = true, action: Action): boolean => {
  switch (action.type) {
    case User_PassedIntroduction:
      return action.payload.hasPassed;

    default:
      return state;
  }
};
