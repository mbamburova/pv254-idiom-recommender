import {IQuestion} from '../../models/Question';
import {IQuestionRepository} from '../../repositories/interfaces/IQuestionRepository';

export interface IQuestionStoreState {
  readonly questionRepository: IQuestionRepository;
  readonly currentQuestion: IQuestion | null;
  readonly correctAnswerId: string | null;
  readonly selectedAnswerId: string | null;
}
