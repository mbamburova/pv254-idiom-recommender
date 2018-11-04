import {correctAnswerLoaded} from '../appActions';
import {Dispatch} from 'redux';
import {IQuestionRepository} from '../../repositories/interfaces/IQuestionRepository';

export async function createSelectAnswerAction(questionRepository: IQuestionRepository, questionId: string, selectedAnswerId: string, dispatch: Dispatch) {
  await new Promise(resolve => setTimeout(resolve, 1000));
  const correctness = await questionRepository.answerQuestion(questionId, selectedAnswerId);
  dispatch(correctAnswerLoaded(correctness.correct_answer_id));
}
