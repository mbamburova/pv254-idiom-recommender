import {ICurrentUserRepository} from '../../repositories/interfaces/ICurrentUserRepository';
import {getUserFromServerModel} from '../../models/User';
import {userInitialized} from '../appActions';
import {Dispatch} from 'redux';

export async function createInitUserAction(currentUserRepository: ICurrentUserRepository, dispatch: Dispatch) {
    await new Promise(resolve => setTimeout(resolve, 1000));
    const user = await currentUserRepository.newUser();
    const currentUser = getUserFromServerModel(user);
    dispatch(userInitialized(currentUser));
}
