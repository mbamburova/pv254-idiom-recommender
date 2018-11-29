import {answerSelected, correctAnswerLoaded} from '../appActions';
import {Dispatch} from 'redux';
import {IQuestionRepository} from '../../repositories/interfaces/IQuestionRepository';
import {createGenerateQuestionAction} from './generateQuestion';
import {IUser} from '../../models/User';

const WAITING_TIME_MS = 2000;

export async function createSelectAndLoadAnswerAction(questionRepository: IQuestionRepository, currentUser: IUser,
                                                      questionId: number, selectedAnswerId: number, dispatch: Dispatch) {
  dispatch(answerSelected(selectedAnswerId));
  const correctness = await questionRepository.answerQuestion(currentUser, questionId, selectedAnswerId);
  dispatch(correctAnswerLoaded(correctness.correct_answer_id));
  await new Promise(resolve => setTimeout(resolve, WAITING_TIME_MS));
  await createGenerateQuestionAction(questionRepository, currentUser, dispatch);
}
