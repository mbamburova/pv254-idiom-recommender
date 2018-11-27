import {IQuestionStoreState} from './IQuestionStoreState';
import {combineReducers} from 'redux';
import {currentQuestion} from './currentQuestion';
import {selectedAnswerId} from './selectedAnswerId';
import {correctAnswerId} from './correctAnswerId';
import {questionRepository} from '../../repositories/questionRepository';

export const questionReducer = combineReducers<IQuestionStoreState>({
  questionRepository: () => questionRepository,
  currentQuestion,
  correctAnswerId,
  selectedAnswerId,
});
