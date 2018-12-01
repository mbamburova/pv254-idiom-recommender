import * as React from 'react';
import {IUser} from '../models/User';
import {Question} from '../containers/Question';
import {ICurrentUserRepository} from '../repositories/interfaces/ICurrentUserRepository';
import {IQuestionRepository} from '../repositories/interfaces/IQuestionRepository';
import {AnswerList} from '../containers/AnswerList';
import {Introduction} from '../containers/Introduction';

export interface IAppStateProps {
  loaded: boolean;
  hasUserPassedIntroduction: boolean;
  currentUser: IUser | null;
  userRepository: ICurrentUserRepository;
  questionRepository: IQuestionRepository;
}

export interface IAppCallbackProps {
  initUser: (userRepository: ICurrentUserRepository) => Promise<void>;
  generateQuestion: (questionRepository: IQuestionRepository, user: IUser) => Promise<void>;
}

export type AppProps = IAppStateProps & IAppCallbackProps;

export class AppComponent extends React.PureComponent<AppProps> {
  static displayName = 'IdiomApp';

  render() {
    if (!this.props.loaded) {
      if (this.props.currentUser == null) {
        this.props.initUser(this.props.userRepository);
      }
      else {
        this.props.generateQuestion(this.props.questionRepository, this.props.currentUser);
      }

      return (
        <div className="loader">
          <div className="loader__bubble" />
        </div>);
    }
    return (
      <div className="container text-center" style={{paddingTop: '5em'}}>
        <Introduction/>
        <Question/>
        <AnswerList/>
      </div>
    );
  }
}
