import { connect } from 'react-redux';
import {AppComponent,  IAppCallbackProps, IAppStateProps} from '../components/App';
import {ComponentClass} from 'react';
import {IStore} from '../reducers/IStore';
import {Dispatch} from 'redux';
import {createInitUserAction} from '../actions/thunks/initUser';
import {ICurrentUserRepository} from '../repositories/interfaces/ICurrentUserRepository';
import {createGenerateQuestionAction} from '../actions/thunks/generateQuestion';

const mapStateToProps = (state: IStore): IAppStateProps => {
  return {
    loaded: state.questionStore.currentQuestion !== null,
    hasUserPassedIntroduction: state.userStore.hasUserPassedIntroduction,
    currentUser: state.userStore.currentUser,
    userRepository: state.userStore.userRepository,
    questionRepository: state.questionStore.questionRepository,
  };
};

const mapDispatchToProps = (dispatch: Dispatch): IAppCallbackProps => {
  return {
    initUser: (userRepository: ICurrentUserRepository) => createInitUserAction(userRepository, dispatch),
    generateQuestion: ((questionRepository, user) => createGenerateQuestionAction(questionRepository, user, dispatch)),
  };
};

export const App: ComponentClass =
  connect(mapStateToProps, mapDispatchToProps)(AppComponent);
