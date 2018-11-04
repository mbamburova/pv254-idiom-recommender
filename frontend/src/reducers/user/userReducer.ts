import {combineReducers} from 'redux';
import {IUserStoreState} from './IUserStoreState';
import {currentUser} from './currentUser';
import {fakeCurrentUserRepository} from '../../repositories/fakes/fakeCurrentUserRepository';

export const userReducer = combineReducers<IUserStoreState>({
  userRepository: () => fakeCurrentUserRepository,
  currentUser,
});
