import {IQuestionStoreState} from './IQuestionStoreState';
import {combineReducers} from 'redux';
import {currentQuestion} from './currentQuestion';
import {fakeQuestionRepository} from '../../repositories/fakes/fakeQuestionRepository';
import {selectedAnswerId} from './selectedAnswerId';
import {correctAnswerId} from './correctAnswerId';

export const questionReducer = combineReducers<IQuestionStoreState>({
  questionRepository: () => fakeQuestionRepository,
  currentQuestion,
  correctAnswerId,
  selectedAnswerId,
});
