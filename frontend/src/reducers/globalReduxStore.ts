import {combineReducers} from 'redux';
import { IStore } from './IStore';
import {userReducer} from './user/userReducer';
import {questionReducer} from './question/questionReducer';

export const rootReducer = combineReducers<IStore>({
  userStore: userReducer,
  questionStore: questionReducer,
});

