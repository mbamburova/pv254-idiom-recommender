import {CurrentUserServerModel} from '../repositories/serverModels/CurrentUserServerModel';

export type IUser = {
  readonly id: string;
  readonly version: string;
};

export function getUserFromServerModel(serverModel: CurrentUserServerModel): IUser {
  return {
    id: serverModel.user_id,
    version: serverModel.rec_version,
  };
}

export function userToServerModel(user: IUser): CurrentUserServerModel {
  return {
    user_id: user.id,
    rec_version: user.version,
  };
}
