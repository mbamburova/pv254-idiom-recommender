import { connect } from 'react-redux';
import {ComponentClass} from 'react';
import {IStore} from '../reducers/IStore';
import {Dispatch} from 'redux';
import {AnswerListComponent, IAnswerListCallbackProps, IAnswerListStateProps} from '../components/AnswerList';
import {createSelectAndLoadAnswerAction} from '../actions/thunks/selectAndLoadAnswer';

const mapStateToProps = (state: IStore): IAnswerListStateProps => {
  const currentQuestion = state.questionStore.currentQuestion;
  const currentUser = state.userStore.currentUser;
  if (currentQuestion === null || currentUser === null) {
    throw new Error('Answer list created before question loaded');
  }
  return {
    questionRepository: state.questionStore.questionRepository,
    answers: currentQuestion.answers,
    questionId: currentQuestion.id,
    selectedAnswerId: state.questionStore.selectedAnswerId,
    correctAnswerId: state.questionStore.correctAnswerId,
    currentUser,
  };
};

const mapDispatchToProps = (dispatch: Dispatch): IAnswerListCallbackProps => {
  return {
    onAnswerSelect: (questionRepository, currentUser, questionId, answerId) => createSelectAndLoadAnswerAction(questionRepository, currentUser, questionId, answerId, dispatch),
  };
};

export const AnswerList: ComponentClass =
  connect(mapStateToProps, mapDispatchToProps)(AnswerListComponent);
