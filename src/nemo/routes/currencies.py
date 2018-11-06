import json
import re

from flask import Blueprint, request, Response, jsonify, abort

from nemo.models.db import session_scope
from nemo.models.schema import Currency

CURRENCIES_BP = Blueprint('currencies', __name__)

ISO4217_CODE_REGEX = re.compile('^[A-Z]{3}$')

@CURRENCIES_BP.route('/v1/currencies', methods=['GET'])
def list_currencies():
    """List currencies."""
    with session_scope() as session:
        currencies = session.query(Currency)

    currencies = map(map_currency, currencies)

    return jsonify({
        'currencies': list(currencies)
    })

@CURRENCIES_BP.route('/v1/currencies', methods=['POST'])
def create_currency():
    """Create new currency"""
    currency_json = request.get_json()

    try:
        iso4217_code = currency_json['iso4217_code']
        title = currency_json['title']
        symbol = currency_json['symbol']
        long_symbol = currency_json['long_symbol']
        display_factor = currency_json['display_factor'] if 'display_factor' in currency_json else 0

        assert iso4217_code is not None
        assert ISO4217_CODE_REGEX.match(iso4217_code)
        assert title is not None
        assert title
        assert symbol is not None
        assert len(symbol) == 1
        assert long_symbol is not None
        assert len(long_symbol) == 3
        assert display_factor is not None
        assert display_factor >= 0
    except (AssertionError, KeyError):
        abort(400)

    currency = Currency(
        iso4217_code=iso4217_code,
        title=title,
        symbol=symbol,
        long_symbol=long_symbol,
        display_factor=display_factor
    )

    with session_scope() as session:
        session.add(currency)
        currency_path = '/v1/currencies/{}'.format(currency.iso4217_code)
        currency_json = map_currency(currency)

    resp = Response()
    resp.headers['Location'] = currency_path
    resp.status_code = 201
    resp.data = json.dumps(currency_json)
    resp.headers['Content-Type'] = 'application/json'

    return resp

@CURRENCIES_BP.route('/v1/currencies/<string:currency_code>', methods=['GET'])
def retreive_currency(currency_code):
    if not ISO4217_CODE_REGEX.match(currency_code):
        abort(404)

    with session_scope() as session:
        currency_json = map_currency(
            session.query(Currency) \
                .filter(Currency.iso4217_code == currency_code) \
                .one()
        )

    return jsonify(currency_json)

def map_currency(currency):
    return {
        'iso4217_code': currency.iso4217_code,
        'title': currency.title,
        'symbol': currency.symbol,
        'long_symbol': currency.long_symbol,
        'display_factor': currency.display_factor,
    }
