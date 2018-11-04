import {IUser} from '../../models/User';
import {Action} from '../../models/Action';
import {User_Initialized} from '../../actions/actionTypes';

export const currentUser = (state: IUser | null = null, action: Action): IUser | null => {
  switch (action.type) {
    case User_Initialized:
      return action.payload.user;

    default:
      return state;
  }
};
