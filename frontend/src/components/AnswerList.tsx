import * as React from 'react';
import {IAnswer} from '../models/Answer';
import {List} from 'immutable';
import {IQuestionRepository} from '../repositories/interfaces/IQuestionRepository';
import {Answer} from './Answer';
import {IUser} from '../models/User';

export interface IAnswerListStateProps {
  questionRepository: IQuestionRepository;
  answers: List<IAnswer>;
  questionId: string;
  selectedAnswerId: string | null;
  correctAnswerId: string | null;
  currentUser: IUser;
}

export interface IAnswerListCallbackProps {
  onAnswerSelect: (questionRepository: IQuestionRepository, user: IUser, questionId: string, answerId: string) => Promise<void>;
}

export type AnswerListProps = IAnswerListStateProps & IAnswerListCallbackProps;

export class AnswerListComponent extends React.PureComponent<AnswerListProps> {
  static displayName = 'AnswerList';

  render() {
    const { questionRepository, currentUser, answers, questionId, selectedAnswerId, correctAnswerId, onAnswerSelect } = this.props;
    return (
      <table>
        <tbody>
        {
          answers.map((answer: IAnswer) => {
            const callback = () => onAnswerSelect(questionRepository, currentUser, questionId, answer.id);
            const isCorrect = !!correctAnswerId && correctAnswerId === answer.id;
            const isSelected = !!selectedAnswerId && selectedAnswerId === answer.id;
            return <Answer key={answer.id} text={answer.text} isSelected={isSelected} isCorrect={isCorrect} onAnswerSelect={callback}/>;
          })
        }
        </tbody>
      </table>
    );
  }
}
