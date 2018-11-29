import {combineReducers} from 'redux';
import {IUserStoreState} from './IUserStoreState';
import {currentUser} from './currentUser';
import {currentUserRepository} from '../../repositories/currentUserRepository';

export const userReducer = combineReducers<IUserStoreState>({
  userRepository: () => currentUserRepository,
  currentUser,
});
