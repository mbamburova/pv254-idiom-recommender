import {ICurrentUserRepository} from '../interfaces/ICurrentUserRepository';
import {CurrentUserServerModel} from '../serverModels/CurrentUserServerModel';

export const fakeCurrentUserRepository: ICurrentUserRepository = {
  newUser: (): Promise<CurrentUserServerModel> => {
    return Promise.resolve( {
        id: 10,
        version: 'A',
      }
    );
  }
};
