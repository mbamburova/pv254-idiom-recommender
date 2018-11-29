import {IQuestionStoreState} from './question/IQuestionStoreState';
import {IUserStoreState} from './user/IUserStoreState';

export interface IStore {
  readonly questionStore: IQuestionStoreState;
  readonly userStore: IUserStoreState;
}
