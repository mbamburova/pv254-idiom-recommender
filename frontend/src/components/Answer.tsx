import * as React from 'react';

export type AnswerProps = {
  text: string;
  isSelected: boolean;
  isCorrect: boolean;
  disabled: boolean;
  onAnswerSelect: () => Promise<void>;
};

export class Answer extends React.PureComponent<AnswerProps> {
  static displayName = 'Answer';

  render() {
    let className;
    if (this.props.isCorrect) {
      className = 'btn-success';
    }
    else if (this.props.isSelected) {
      className = 'btn-danger';
    }
    else {
      className = 'btn-secondary';
    }
    return (
      <tr>
        <td>
          <button
            type="button"
            className={`btn ${className} btn-lg btn-block`}
            style={{cursor: 'auto', whiteSpace: 'normal' }}
            disabled={this.props.disabled}
            onClick={this.props.onAnswerSelect}
          >
            {this.props.text}
          </button>
        </td>
      </tr>
    );
  }
}
