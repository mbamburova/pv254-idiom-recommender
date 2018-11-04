import { connect } from 'react-redux';
import {IQuestionProps, QuestionComponent} from '../components/Question';
import {ComponentClass} from 'react';
import {IStore} from '../reducers/IStore';

const mapToProps = (state: IStore): IQuestionProps => {
  const currentQuestion = state.questionStore.currentQuestion;
  return {
    text: (currentQuestion === null) ? null : currentQuestion.question,
  };
};

export const Question: ComponentClass =
  connect<IQuestionProps>(mapToProps)(QuestionComponent);

