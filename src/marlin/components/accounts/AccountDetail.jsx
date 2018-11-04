import React, { Component } from 'react';

export default class AccountDetail extends Component {
    render() {
        return (
            <div>
                <h2>
                    Account Detail
                    <small className='text-muted'>
                        This would probably be the account name in the real application
                    </small>
                </h2>
                <h4>The account ID is {this.props.match.params.id}</h4>
            </div>
        );
    }
}