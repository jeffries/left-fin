import { types } from 'Actions/accounts';

const initialState = {
    accounts: []
};

export default (state = initialState, { type, payload }) => {
    switch (type) {
    case types.ACCOUNTS_LOAD:
        return { ...state, accounts: payload };
    default:
        return state;
    }
};
