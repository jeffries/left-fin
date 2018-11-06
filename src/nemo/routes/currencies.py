import json
import re

from flask import Blueprint, request, Response, jsonify, abort

from nemo.models.db import session_scope
from nemo.models.schema import Currency

currencies_bp = Blueprint('currencies', __name__)

currency_re = re.compile('^[A-Z]{3}$')

@currencies_bp.route('/v1/currencies', methods=['GET'])
def list_currencies():
    with session_scope() as s:
        currencies = s.query(Currency)

    currencies = map(map_currency, currencies)

    return jsonify({
        'currencies': list(currencies)
    })

@currencies_bp.route('/v1/currencies', methods=['POST'])
def create_currency():
    currency_json = request.get_json()

    try:
        iso4217_code = currency_json['iso4217_code']
        title = currency_json['title']
        symbol = currency_json['symbol']
        long_symbol = currency_json['long_symbol']
        display_factor = currency_json['display_factor'] if 'display_factor' in currency_json else 0

        assert iso4217_code is not None
        assert currency_re.match(iso4217_code)
        assert title is not None
        assert len(title) > 0
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

    with session_scope() as s:
        s.add(currency)
        c_path = '/v1/currencies/{}'.format(currency.iso4217_code)
        c = map_currency(currency)

    r = Response()
    r.headers['Location'] = c_path
    r.status_code = 201
    r.data = json.dumps(c)
    r.headers['Content-Type'] = 'application/json'

    return r

@currencies_bp.route('/v1/currencies/<string:currency_code>', methods=['GET'])
def retreive_currency(currency_code):
    if not currency_re.match(currency_code):
        abort(404)

    with session_scope() as s:
        c = map_currency(s.query(Currency).filter(Currency.iso4217_code == currency_code).one())

    return jsonify(c)

def map_currency(c):
    return {
        'iso4217_code': c.iso4217_code,
        'title': c.title,
        'symbol': c.symbol,
        'long_symbol': c.long_symbol,
        'display_factor': c.display_factor,
    }
