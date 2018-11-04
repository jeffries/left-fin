import 'bootstrap'; 
import 'bootstrap/scss/bootstrap'; // bootstrap default styles

import React from 'react';
import ReactDOM from 'react-dom';

import { Provider } from 'react-redux';
import store from './store';

import App from './components/App';

ReactDOM.render((
    <Provider store={store}>
        <App />
    </Provider>
), document.getElementById('app-mount'));
