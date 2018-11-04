import * as React from 'react';
import {IAnswer} from '../models/Answer';
import {List} from 'immutable';
import {IQuestionRepository} from '../repositories/interfaces/IQuestionRepository';

export interface IAnswerListProps {
  questionRepository: IQuestionRepository;
  answers: List<IAnswer>;
  selectedAnswer: string | null;
  correctAnswer: string | null;
}

export interface IAnswerListCallbackProps {
  onAnswerSelect: (questionRepository: IQuestionRepository, questionId: string, answerId: string) => Promise<void>;
}

export type AnswerListProps = IAnswerListCallbackProps & IAnswerListCallbackProps;

export class AnswerListComponent extends React.PureComponent<AnswerListProps> {
  static displayName = 'AnswerList';

  render() {

    return (
      <h1>
        x
      </h1>
    );
  }
}
