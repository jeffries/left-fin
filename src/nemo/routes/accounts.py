import json

from flask import Blueprint, render_template, jsonify, request, Response, abort
from sqlalchemy.orm.exc import NoResultFound

from nemo.models.db import session_scope
from nemo.models.schema import Account, InstitutionAccount, PersonalAccount, Currency

accounts_bp = Blueprint('accounts', __name__)

@accounts_bp.route('/v1/accounts', methods=['GET'])
def list_accounts():
    with session_scope() as s:
        ia = map(map_ia, s.query(InstitutionAccount).all())
        pa = map(map_pa, s.query(PersonalAccount).all())

    return jsonify({
        'accounts': list(list(ia) + list(pa))
    })

@accounts_bp.route('/v1/accounts', methods=['POST'])
def create_account():
    account_json = request.get_json()

    account_type = account_json['type']
    
    if account_type == 'institution_account':
        title = str(account_json['title'])
        institution_title = str(account_json['institution_title'])
        number_suffix = str(int(account_json['number_suffix']))
        minimum_value = int(account_json['minimum_value'])

        # account and institution title must be present
        if title is None or \
                len(title) <= 0 or \
                institution_title is None or \
                len(institution_title) <= 0:
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

    with session_scope() as s:
        currency = s.query(Currency).filter(Currency.iso4217_code == currency_code).one()
        s.add(account)
        account.currency = currency
        s.commit()

        a_path = '/v1/accounts/{}'.format(account.id)
        a = map_account(account)

    r = Response()
    r.headers['Location'] = a_path
    r.status_code = 201
    r.data = json.dumps(a)
    r.headers['Content-Type'] = 'application/json'

    return r

@accounts_bp.route('/v1/accounts/<int:account_id>', methods=['GET'])
def retreive_account(account_id):
    with session_scope() as s:
        try:
            account = s.query(Account).filter(Account.id == account_id).one()
        except NoResultFound:
            abort(404)

        if account.type == 'institution_account':
            account = s.query(InstitutionAccount).filter(Account.id == account_id).one()

            account_json = map_ia(account)
        elif account.type == 'personal_account':
            account = s.query(PersonalAccount).filter(Account.id == account_id).one()

            account_json = map_pa(account)

    return jsonify(account_json)

def map_ia(a):
    return {
        'id': a.id,
        'type': a.type,
        'currency': a.currency.iso4217_code,
        'minimum_value': a.minimum_value,
        'number_suffix': a.number_suffix,
        'title': a.title,
        'institution_title': a.institution_title
    }

def map_pa(a):
    return {
        'id': a.id,
        'type': a.type,
        'currency': a.currency.iso4217_code,
        'holder': a.holder
    }

def map_account(a):
    if a.type == 'institution_account':
        return map_ia(a)
    elif a.type == 'personal_account':
        return map_pa(a)
    else:
        raise ValueError('bad account type')
