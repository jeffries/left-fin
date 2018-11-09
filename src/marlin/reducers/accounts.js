import { types } from 'Actions/accounts';

const initialState = {
    accounts: []
};

export default (state = initialState, { type, payload }) => {
    switch (type) {
    case types.ACCOUNTS_SET:
        return { ...state, accounts: payload };
    case types.ACCOUNT_UPDATE:
        console.log(payload);
        return { ...state };
    default:
        return state;
    }
};
