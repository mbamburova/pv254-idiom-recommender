import {combineReducers} from 'redux';
import {IUserStoreState} from './IUserStoreState';
import {currentUser} from './currentUser';
import {currentUserRepository} from '../../repositories/currentUserRepository';
import {hasUserPassedIntroduction} from './hasUserPassedIntroduction';

export const userReducer = combineReducers<IUserStoreState>({
  userRepository: () => currentUserRepository,
  currentUser,
  hasUserPassedIntroduction
});
