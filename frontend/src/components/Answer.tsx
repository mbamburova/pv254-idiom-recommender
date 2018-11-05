import * as React from 'react';

export type AnswerProps = {
  text: string;
  isSelected: boolean;
  isCorrect: boolean;
  onAnswerSelect: () => Promise<void>;
};

export class Answer extends React.PureComponent<AnswerProps> {
  static displayName = 'Answer';

  render() {
    let buttonStyle;
    if (this.props.isCorrect) {
      buttonStyle = {
        backgroundColor: '#4CAF50',
        color: 'white',
      };
    } else if (this.props.isSelected) {
      buttonStyle = {
        backgroundColor: '#cc0000',
        color: 'white',
      };    } else {
      buttonStyle = {
        backgroundColor: 'white',
        color: 'black',
      };    }
    return (
      <tr>
        <td>
          <button type="button" style={buttonStyle} onClick={this.props.onAnswerSelect}>
            {this.props.text}
          </button>
        </td>
      </tr>
    );
  }
}
