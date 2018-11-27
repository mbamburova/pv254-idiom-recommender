import {IQuestion} from '../../models/Question';
import {IQuestionRepository} from '../../repositories/interfaces/IQuestionRepository';

export interface IQuestionStoreState {
  readonly questionRepository: IQuestionRepository;
  readonly currentQuestion: IQuestion | null;
  readonly correctAnswerId: number | null;
  readonly selectedAnswerId: number | null;
}
