import 'bootstrap/scss/bootstrap'; // bootstrap default styles
import 'bootstrap'; 

import React from 'react';
import ReactDOM from 'react-dom';

import { BrowserRouter } from 'react-router-dom';
import { Provider } from 'react-redux';
import store from './store';

import App from './components/App';

console.log('rendering application');

ReactDOM.render((
    <Provider store={store}>
        <BrowserRouter>
            <App />
        </BrowserRouter>
    </Provider>
), document.getElementById('app-mount'));
