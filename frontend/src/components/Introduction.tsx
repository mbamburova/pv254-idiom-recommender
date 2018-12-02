import * as React from 'react';
import {Modal, Button} from 'react-bootstrap';
import {Action} from '../models/Action';

export type IntroStateProps = {
  show: boolean;
};

export type IntroDispatchProps = {
  onClose: (value: boolean) => Action;
};

export type IntroductionProps = IntroDispatchProps & IntroStateProps;

const indentation = {
  margin: '0 0 0 10px',
};

const marginDown = {
  margin: '0 0 10px 0'
};

const buttonStyle = {
  margin: '0 10px 0 0'
};

export class IntroductionComponent extends React.PureComponent<IntroductionProps> {
  _closeHandling = () => {
    return this.props.onClose(false);
  };

  render = () => {
    return (
      <div>
        <Modal show={this.props.show} onHide={this.props.onClose}>
          <Modal.Header>
            <Modal.Title style={indentation}>Introduction</Modal.Title>
          </Modal.Header>
          <Modal.Body style={indentation}>
            <h4>What is waiting for you</h4>
            <p style={marginDown}>
              We have prepared a few questions for you.
              Each question contains an idiomatic expression together with 3 possible meanings.
              Your task is to choose the correct one. There is only one correct answer.
            </p>

            <h4>Take as much time as you need, but it would help us if you answered at least 10 questions.</h4>
            <p>
              When you are done, please click on finish button.
            </p>

            <h4>Last but not least</h4>
            <p>
              At the end of this quiz, there is a link to a short <strong>survey</strong>.
              We would be very happy if you fill it.
            </p>

            <h3>Many thanks!</h3>

          </Modal.Body>
          <Modal.Footer>
            <Button style={buttonStyle} className="btn-info btn-lg" onClick={this._closeHandling}>Got it</Button>
          </Modal.Footer>
        </Modal>
      </div>
    );
  };
}
