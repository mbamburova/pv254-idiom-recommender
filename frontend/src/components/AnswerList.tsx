import * as React from 'react';
import {IAnswer} from '../models/Answer';
import {List} from 'immutable';
import {IQuestionRepository} from '../repositories/interfaces/IQuestionRepository';
import {Answer} from './Answer';
import {IUser} from '../models/User';

export interface IAnswerListStateProps {
  questionRepository: IQuestionRepository;
  answers: List<IAnswer>;
  questionId: number;
  selectedAnswerId: number | null;
  correctAnswerId: number | null;
  currentUser: IUser;
}

export interface IAnswerListCallbackProps {
  onAnswerSelect: ((questionRepository: IQuestionRepository, user: IUser, questionId: number, answerId: number) => Promise<void>);
}

export type AnswerListProps = IAnswerListStateProps & IAnswerListCallbackProps;

export class AnswerListComponent extends React.PureComponent<AnswerListProps> {
  static displayName = 'AnswerList';

  render() {
    const {
      questionRepository, currentUser, answers, questionId, selectedAnswerId, correctAnswerId, onAnswerSelect
    } = this.props;
    return (
      <table style={{margin: '0 auto', borderCollapse: 'separate', borderSpacing: '1em'}}>
        <tbody>
        {
          answers.map((answer: IAnswer) => {
            const callback = () => onAnswerSelect(questionRepository, currentUser, questionId, answer.id);
            const isCorrect = !!correctAnswerId && correctAnswerId === answer.id;
            // don't be incorrect until correctness is not loaded
            const isSelected = !!correctAnswerId && !!selectedAnswerId && selectedAnswerId === answer.id;
            const disabled = selectedAnswerId !== null;
            return <Answer key={answer.id} text={answer.text} isSelected={isSelected} isCorrect={isCorrect} disabled={disabled} onAnswerSelect={callback}/>;
          })
        }
        </tbody>
      </table>
    );
  }
}
