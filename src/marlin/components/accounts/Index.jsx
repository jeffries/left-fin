import React, { Component } from 'react';

import { Route } from 'react-router-dom';

import AccountHome from './AccountHome'
import AccountDetail from './AccountDetail';

export default class Accounts extends Component {
    render() {
        return (
            <div>
                <Route path={this.props.match.url} exact component={AccountHome} />
                <Route path={`${this.props.match.url}/:id`} exact component={AccountDetail} />
            </div>
        );
    }
}
