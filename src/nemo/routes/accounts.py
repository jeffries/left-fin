import json

from flask import Blueprint, jsonify, request, Response, abort
from sqlalchemy.orm.exc import NoResultFound

from nemo.models.db import session_scope
from nemo.models.schema import Account, InstitutionAccount, PersonalAccount, Currency

ACCOUNTS_BP = Blueprint('accounts', __name__)

@ACCOUNTS_BP.route('/v1/accounts', methods=['GET'])
def list_accounts():
    """Retreive a listing of accounts"""
    with session_scope() as session:
        inst_acc = map(map_ia, session.query(InstitutionAccount).all())
        personal_acc = map(map_pa, session.query(PersonalAccount).all())

    return jsonify({
        'accounts': list(list(inst_acc) + list(personal_acc))
    })

@ACCOUNTS_BP.route('/v1/accounts', methods=['POST'])
def create_account():
    """Create a new account"""
    account_json = request.get_json()

    account_type = account_json['type']

    if account_type == 'institution_account':
        title = str(account_json['title'])
        institution_title = str(account_json['institution_title'])
        number_suffix = str(int(account_json['number_suffix']))
        minimum_value = int(account_json['minimum_value'])

        # account and institution title must be present
        if not title or not institution_title:
            raise ValueError('account and institution titles are required')

        account = InstitutionAccount(
            title=title,
            institution_title=institution_title,
            number_suffix=number_suffix,
            minimum_value=minimum_value
        )
    elif account_type == 'personal_account':
        holder = str(account_json['holder'])

        if holder is None or len(holder) <= 0:
            raise ValueError('holder is required')

        account = PersonalAccount(
            holder=holder
        )
    else:
        raise ValueError('invalid account type')

    currency_code = account_json['currency']

    with session_scope() as session:
        currency = session.query(Currency).filter(Currency.iso4217_code == currency_code).one()
        session.add(account)
        account.currency = currency
        session.commit()

        account_path = '/v1/accounts/{}'.format(account.id)
        account_json = map_account(account)

    resp = Response()
    resp.headers['Location'] = account_path
    resp.status_code = 201
    resp.data = json.dumps(account_json)
    resp.headers['Content-Type'] = 'application/json'

    return resp

@ACCOUNTS_BP.route('/v1/accounts/<int:account_id>', methods=['GET'])
def retreive_account(account_id):
    """Retrieve a particular account"""
    with session_scope() as session:
        try:
            account = session.query(Account).filter(Account.id == account_id).one()
        except NoResultFound:
            abort(404)

        if account.type == 'institution_account':
            account = session.query(InstitutionAccount).filter(Account.id == account_id).one()

            account_json = map_ia(account)
        elif account.type == 'personal_account':
            account = session.query(PersonalAccount).filter(Account.id == account_id).one()

            account_json = map_pa(account)

    return jsonify(account_json)

def map_ia(acc):
    """Map an institutional account from sqlalchemy object to JSON representation"""
    return {
        'id': acc.id,
        'type': acc.type,
        'currency': acc.currency.iso4217_code,
        'minimum_value': acc.minimum_value,
        'number_suffix': acc.number_suffix,
        'title': acc.title,
        'institution_title': acc.institution_title
    }

def map_pa(acc):
    """Map a personal account from sqlalchemy object to JSON representation"""
    return {
        'id': acc.id,
        'type': acc.type,
        'currency': acc.currency.iso4217_code,
        'holder': acc.holder
    }

def map_account(acc):
    """Map an account from sqlalchemy object to JSON representation"""
    if acc.type == 'institution_account':
        return map_ia(acc)
    elif acc.type == 'personal_account':
        return map_pa(acc)
    else:
        raise ValueError('bad account type')
