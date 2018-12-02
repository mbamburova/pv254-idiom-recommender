import { connect } from 'react-redux';
import {IStore} from '../reducers/IStore';
import {Dispatch} from 'redux';
import {passIntroduction} from '../actions/appActions';
import {ComponentClass} from 'react';
import {IntroductionComponent} from '../components/Introduction';

const mapStateToProps = (state: IStore) => ({
  show: state.userStore.hasUserPassedIntroduction
});

const mapDispatchToProp = (dispatch: Dispatch) => ({
  onClose: (value: boolean) => dispatch(passIntroduction(value))
});

export const Introduction: ComponentClass =
  connect(mapStateToProps, mapDispatchToProp)(IntroductionComponent);
