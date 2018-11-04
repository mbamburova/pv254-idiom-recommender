import * as React from 'react';

export interface IQuestionProps {
  text?: string | null;
}

export class QuestionComponent extends React.PureComponent<IQuestionProps> {
  static displayName = 'Question';

  render() {
    const { text } = this.props;

    return (
      <h1>
        {text}
      </h1>
    );
  }
}
