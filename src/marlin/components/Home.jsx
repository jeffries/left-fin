import React, { Component } from 'react';

import { Link } from 'react-router-dom';

export default class Home extends Component {
    render() {
        return (
            <div className='row'>
                <div className='col-12'>
                    <h1 className='display-3'>Welcome to Nemo.</h1>
                    <h2>Nemo is a personal financial manager.</h2>
                    <ul>
                        <li>Currencies</li>
                        <li>
                            <Link to='/accounts'>
                                Accounts
                            </Link>
                        </li>
                        <li>Transactions</li>
                    </ul>
                </div>
            </div>
        );
    }
}
