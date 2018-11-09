import React, { Component } from 'react';

import { Route } from 'react-router-dom';

import AccountHome from './AccountHome';
import AccountDetail from './AccountDetail';

export default class Accounts extends Component {
    render() {
        return [
            <Route key='home' path={this.props.match.url} exact component={AccountHome} />,
            <Route key='detail' path={`${this.props.match.url}/:id`} component={AccountDetail} />
        ];
    }
}
