import { mirror, prepend, payloadCreator } from './util';

export const types = {
    /* For use when data is changed by the user */
    ...mirror(prepend([
        'ADD',
        'DELETE',
        'UPDATE',
    ], 'ACCOUNT')),
    /* For use when data is loaded from the server */
    ...mirror(prepend([
        'LOAD'
    ], 'ACCOUNTS')),
};

export const loadAccounts = payloadCreator(types.ACCOUNTS_LOAD);
export const addAccount = payloadCreator(types.ACCOUNT_ADD);
