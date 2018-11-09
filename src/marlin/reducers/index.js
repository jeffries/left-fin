import { combineReducers } from 'redux';
import accounts from './accounts';

const reducer = combineReducers({ accounts });

export default function(state, action) {
    console.log(state);
    console.log(action);
    const newState = reducer(state, action);
    return newState;
};
