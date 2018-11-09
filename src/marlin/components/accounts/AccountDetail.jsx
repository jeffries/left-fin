import React, { Component } from 'react';

import { connect } from 'react-redux';

import { updateAccount } from 'Actions/accounts';

class AccountDetail extends Component {
    constructor(props) {
        super(props);

        this._handleTypeChange = this._handleTypeChange.bind(this);
    }

    render() {
        return (
            <div className='row'>
                <div className='col-12'>
                    <h2>
                        Account Detail
                    </h2>
                </div>
                <div className='col-12'>
                <form>
                    <div className='container'>
                    <div className='row'>
                        {this._renderTypeGroup()}
                        {this._renderAccountDetailGroups()}
                    </div>
                    </div>
                </form>
                </div>
            </div>
        );
    }

    _handleTypeChange(event) {
        this.props.updateAccount({ type: event.target.value });
    }

    _renderTypeGroup() {
        let opts = [
            ['Institutional', 'institution_account'],
            ['Personal', 'personal_account'],
        ];

        if (true) { // TODO make this depend on whether a type is set or not
            opts = [
                ['', ''],
                ...opts
            ];
        }

        return (
            <div className='col-md-6 form-group' key='type-group'>
                <label htmlFor='type'>Type</label>
                <select
                        name='type'
                        className='form-control'
                        onChange={this._handleTypeChange}
                        value={this.props.account.type}>
                    {opts.map(([v, k]) => (<option value={k} key={k}>{v}</option>))}
                </select>
            </div>
        );
    }

    _renderAccountDetailGroups() {
        return [
            <div className='col-md-6 form-group' key='title-group'>
                <label htmlFor='title'>Title</label>
                <input type='text' name='title' placeholder='Title' className='form-control' />
            </div>
        ]
    }
}

const mapStateToProps = (state, ownProps) => {
    if (ownProps.new) {
        // this is a new account
    }
    else if (ownProps.match.params.id) {
        // this account exists. grab it from the store
        return {
            account: state.accounts.accounts.find((a) => a.id == ownProps.match.params.id)
        };
    }
};
const mapDispatchToProps = (dispatch, ownProps) => {
    if (ownProps.new) {
        // this is a new account
    }
    else if (ownProps.match.params.id) {
        // this account exists. grab it from the store
        return {
            updateAccount: account => dispatch(updateAccount({
                id: ownProps.match.params.id,
                ...account,
            })),
        };
    }
}

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(AccountDetail);
