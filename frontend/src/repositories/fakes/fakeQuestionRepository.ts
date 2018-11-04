import {IQuestionRepository} from '../interfaces/IQuestionRepository';
import {QuestionServerModel} from '../serverModels/QuestionServerModel';
import {CorrectnessServerModel} from '../serverModels/CorrectnessServerModel';

export const fakeQuestionRepository: IQuestionRepository = {
  getQuestion: (): Promise<QuestionServerModel> => {
    return Promise.resolve({
        question: 'Piece of cake',
        question_id: '134',
        answers: [
          {
            answer_id: '546',
            text: 'Need to choose from two difficult options',
          },
          {
            answer_id: '341',
            text: 'An easy task',
          },
          {
            answer_id: '643',
            text: 'Very good food',
          }
        ],
        question_type: 5,
      }
    );
  },
  answerQuestion: (): Promise<CorrectnessServerModel> => {
    return Promise.resolve({
        correct: true,
        correct_answer_id: '341',
      }
    );
  }
};
