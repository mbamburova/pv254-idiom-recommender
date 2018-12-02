import {IUser} from '../models/User';
import {Action} from '../models/Action';
import {Question_Correct_Answer_Loaded, Question_Answer_Selected, Question_Generated, User_Initialized, User_PassedIntroduction} from './actionTypes';
import {IQuestion} from '../models/Question';

export const userInitialized = (user: IUser): Action => ({
  type: User_Initialized,
  payload: {
    user,
  }
});

export const passIntroduction = (hasPassed: boolean): Action => ({
  type: User_PassedIntroduction,
  payload: {
    hasPassed,
  }
});

export const questionGenerated = (question: IQuestion): Action => ({
  type: Question_Generated,
  payload: {
    question,
  }
});

export const answerSelected = (answerId: number): Action => ({
  type: Question_Answer_Selected,
  payload: {
    answerId,
  }
});

export const correctAnswerLoaded = (answerId: number): Action => ({
  type: Question_Correct_Answer_Loaded,
  payload: {
    answerId,
  }
});

