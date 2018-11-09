import React, { Component } from 'react';

import { Link } from 'react-router-dom';
import { connect } from 'react-redux';
import { getAccounts } from 'Api/accounts';
import { setAccounts } from 'Actions/accounts';

class AccountHome extends Component {
    render() {
        return (
            <div className='row'>
                <div className='col-12'>
                    <h2>Accounts</h2>
                    <table className='table'>
                        <tbody>
                            <tr>
                                <th>Title</th>
                                <th>Type</th>
                            </tr>
                            {
                                this.props.accounts.length > 0 ? 
                                this._renderAccountRows() :
                                this._renderLoadingRow()
                            }
                        </tbody>
                    </table>
                </div>
            </div>
        );
    }

    componentDidMount() {
        // Fetch accounts when we mount
        getAccounts()
            .then(resp => resp.json())
            .then(json => this.props.setAccounts(json.accounts))
            .catch(err => console.log(err)); // TODO handle this error better
    }

    _renderAccountRows() {
        return this.props.accounts.map(a => {
            switch (a.type) {
            case 'institution_account':
                return (
                    <tr key={a.id}>
                        <td>
                            <Link to={`/accounts/${a.id}`}>
                                {a.title}
                            </Link>
                        </td>
                        <td>Institutional</td>
                    </tr>
                );
            case 'personal_account':
                return (
                    <tr key={a.id}>
                        <td>
                            <Link to={`/accounts/${a.id}`}>
                                {a.holder}
                            </Link>
                        </td>
                        <td>Personal</td>
                    </tr>
                );
            default:
                console.log('WARNING: got bad account type in AccountHome');
                return null;
            }
        });
    }

    _renderLoadingRow() {
        return (
            <tr>
                <td colSpan='2' className='text-center'>
                    <em>
                        Loading...
                    </em>
                </td>
            </tr>
        );
    }
}

const mapStateToProps = state => ({
    accounts: state.accounts.accounts
});
const mapDispatchToProps = dispatch => ({
    setAccounts: accounts => dispatch(setAccounts(accounts))
});

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(AccountHome);
