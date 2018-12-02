import {IUser} from '../../models/User';
import {ICurrentUserRepository} from '../../repositories/interfaces/ICurrentUserRepository';

export interface IUserStoreState {
  readonly userRepository: ICurrentUserRepository;
  readonly currentUser: IUser | null;
  hasUserPassedIntroduction: boolean;
}
