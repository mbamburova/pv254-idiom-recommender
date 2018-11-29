import {IQuestionRepository} from '../interfaces/IQuestionRepository';
import {QuestionServerModel} from '../serverModels/QuestionServerModel';
import {CorrectnessServerModel} from '../serverModels/CorrectnessServerModel';

export const fakeQuestionRepository: IQuestionRepository = {
  getQuestion: (): Promise<QuestionServerModel> => {
    return Promise.resolve({
        question: 'Piece of cake',
        question_id: 134,
        answers: [
          {
            answer_id: 546,
            answer_text: 'Extremely annoying long text which is going to be displayed weirdly. Need to choose from two difficult options. Extremely annoying long text which is going to be displayed weirdly. Need to choose from two difficult options',
          },
          {
            answer_id: 341,
            answer_text: 'An easy task',
          },
          {
            answer_id: 643,
            answer_text: 'Very good food',
          }
        ],
      }
    );
  },
  answerQuestion: (): Promise<CorrectnessServerModel> => {
    return Promise.resolve({
        correct_answer_id: 341,
      }
    );
  }
};
