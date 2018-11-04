import React, { Component } from 'react';

import { Link } from 'react-router-dom';

export default class AccountHome extends Component {
    render() {
        return (
            <div className='row'>
                <div className='col-12'>
                    <h2>Accounts</h2>
                    <p>
                        This is the account home. Maybe we would show a list of accounts here if this application were working.
                    </p>
                    <p>
                        You can look at an
                        <Link to={`${this.props.match.url}/1`}>
                            account detail page
                        </Link>
                        .
                    </p>
                </div>
            </div>
        );
    }
}