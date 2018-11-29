import {getAnswerFromServerModel, IAnswer} from './Answer';
import {List} from 'immutable';
import {QuestionServerModel} from '../repositories/serverModels/QuestionServerModel';
import {AnswerServerModel} from '../repositories/serverModels/AnswerServerModel';

export interface IQuestion {
  readonly question: string;
  readonly id: number;
  readonly answers: List<IAnswer>;
}

/**
 * Randomly shuffle an array
 * https://stackoverflow.com/a/2450976/1293256
 * @param  {Array} array The array to shuffle
 * @return {String}      The first item in the shuffled array
 */
const shuffle = function<T> (array: T[]) {

  let currentIndex = array.length;
  let temporaryValue, randomIndex;

  // While there remain elements to shuffle...
  while (0 !== currentIndex) {
    // Pick a remaining element...
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex -= 1;

    // And swap it with the current element.
    temporaryValue = array[currentIndex];
    array[currentIndex] = array[randomIndex];
    array[randomIndex] = temporaryValue;
  }

  return array;

};

export function getQuestionFromServerModel(serverModel: QuestionServerModel): IQuestion {
  return {
    question: serverModel.question.charAt(0).toUpperCase() + serverModel.question.slice(1),
    id: serverModel.question_id,
    answers: List(shuffle(serverModel.answers.map((answer: AnswerServerModel) => getAnswerFromServerModel(answer)))),
  };
}
