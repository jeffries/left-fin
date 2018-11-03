import { mirror, prepend } from 'Util';

export const types = {
    ...mirror(prepend([
        'ADD',
        'DELETE',
        'UPDATE',
    ], 'ACCOUNT')),
    ...mirror(prepend([
        'LOAD'
    ], 'ACCOUNTS')),
};

console.log(types);

export const loadAccounts = payload => ({ type: types.ACCOUNTS_LOAD, payload: payload });
