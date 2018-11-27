import {CurrentUserServerModel} from '../repositories/serverModels/CurrentUserServerModel';

export type IUser = {
  readonly id: number;
};

export function getUserFromServerModel(serverModel: CurrentUserServerModel): IUser {
  return {
    id: serverModel.id,
  };
}

export function userToServerModel(user: IUser): CurrentUserServerModel {
  return {
    id: user.id,
  };
}
