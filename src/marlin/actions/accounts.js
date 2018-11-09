import { mirror, prepend, payloadCreator } from './util';

export const types = {
    /* For use when data is changed by the user */
    ...mirror(prepend([
        'UPDATE'
    ], 'ACCOUNT')),
    /* For use when data is loaded from the server */
    ...mirror(prepend([
        'SET'
    ], 'ACCOUNTS')),
};

export const setAccounts = payloadCreator(types.ACCOUNTS_SET);
export const updateAccount = payloadCreator(types.ACCOUNT_UPDATE);
