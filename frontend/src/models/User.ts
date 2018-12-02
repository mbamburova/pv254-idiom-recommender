import {CurrentUserServerModel} from '../repositories/serverModels/CurrentUserServerModel';

export type IUser = {
  readonly id: number;
  readonly version: number;
};

export function getUserFromServerModel(serverModel: CurrentUserServerModel): IUser {
  return {
    id: serverModel.id,
    version: serverModel.version
  };
}

export function userToServerModel(user: IUser): CurrentUserServerModel {
  return {
    id: user.id,
    version: user.version
  };
}
