import {ICurrentUserRepository} from '../interfaces/ICurrentUserRepository';
import {CurrentUserServerModel} from '../serverModels/CurrentUserServerModel';

export const fakeCurrentUserRepository: ICurrentUserRepository = {
  newUser: (): Promise<CurrentUserServerModel> => {
    return Promise.resolve( {
      user_id: 'Newcommer',
      rec_version: 'A',
      }
    );
  }
};
