import {CurrentUserServerModel} from '../serverModels/CurrentUserServerModel';

export interface ICurrentUserRepository {
  newUser: () => Promise<CurrentUserServerModel>;
}
