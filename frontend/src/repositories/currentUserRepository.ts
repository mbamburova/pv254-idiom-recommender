import {SERVER_BASE_URL} from './constants';
import {ICurrentUserRepository} from './interfaces/ICurrentUserRepository';
import {CurrentUserServerModel} from './serverModels/CurrentUserServerModel';

export const currentUserRepository: ICurrentUserRepository = {
  newUser: (): Promise<CurrentUserServerModel> => {
    return fetch(`${SERVER_BASE_URL}/new-user`)
      .then(response => {
        if (!response.ok) {
          throw new Error(response.statusText);
        }
        return response.json();
      });
  }
};
