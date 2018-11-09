import React, { Component } from 'react';
import { Route } from 'react-router-dom';

import Home from 'Components/Home';
import Accounts from 'Components/accounts';
import Currencies from 'Components/currencies';

export default class App extends Component {
    render() {
        return (
            <div>
                <div className='container'>
                    <span className='navigation'></span>
                </div>
                <div className='container'>
                    <Route path='/' exact component={Home} />
                    <Route path='/accounts' component={Accounts} />
                    <Route path='/currencies' component={Currencies} />
                </div>
            </div>
        );
    }
}
