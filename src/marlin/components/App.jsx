import React, { Component } from 'react';
import { BrowserRouter, Route } from 'react-router-dom';

import Home from 'Components/Home';
import Accounts from 'Components/accounts';

export default class App extends Component {
    render() {
        return (
            <BrowserRouter>
                <div>
                    <div className='container'>
                        <span className='navigation'></span>
                    </div>
                    <div className='container'>
                        <Route path='/' exact component={Home} />
                        <Route path='/accounts' component={Accounts} />
                    </div>
                </div>
            </BrowserRouter>
        );
    }
}
