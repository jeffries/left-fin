import json

from util import client

def test_list_currencies(client):
    """List currencies"""

    res = client.get('/v1/currencies')
    assert res.status_code == 200

    data = json.loads(res.data)

    assert 'currencies' in data
    assert len(data['currencies']) == 1

    expected = {
        'display_factor': 2,
        'iso4217_code': 'USD',
        'long_symbol': 'US$',
        'symbol': '$',
        'title': 'United States Dollar'
    }

    for k, v in expected.items():
        assert k in data['currencies'][0]
        assert data['currencies'][0][k] == v

def test_retreive_currency(client):
    """Retreive currency"""

    res = client.get('/v1/currencies/USD')
    assert res.status_code == 200

    data = json.loads(res.data)

    expected = {
        'display_factor': 2,
        'iso4217_code': 'USD',
        'long_symbol': 'US$',
        'symbol': '$',
        'title': 'United States Dollar'
    }

    for k, v in expected.items():
        assert k in data
        assert data[k] == v

def test_retreive_invalid_currency(client):
    """Retrieve currency with an invalid ISO4217 code"""

    res = client.get('/v1/currencies/bad_code')
    assert res.status_code == 404

def test_retreive_miscapitalized_currency(client):
    """Retrieve currency with a miscapitalized ISO4217 code"""

    res = client.get('/v1/currencies/uSd')
    assert res.status_code == 404

def test_retreive_bad_length_currency(client):
    """Retrieve currency with an ISO4217 code with a bad length"""

    res = client.get('/v1/currencies/BADD')
    assert res.status_code == 404

def test_create_currency(client):
    c = {
        'display_factor': 2,
        'iso4217_code': 'EUR',
        'long_symbol': 'EU€',
        'symbol': '€',
        'title': 'Euro'
    }

    res = client.post('/v1/currencies', data=json.dumps(c), headers={
        'Content-Type': 'application/json'
    })
    assert res.status_code == 201
    d1 = json.loads(res.data)

    cpath = res.headers['Location']
    res = client.get(cpath)
    assert res.status_code == 200
    d2 = json.loads(res.data)

    for k, v in c.items():
        assert k in d1
        assert d1[k] == v
        assert k in d2
        assert d2[k] == v

def test_create_currency_no_display_factor(client):
    c = {
        'iso4217_code': 'EUR',
        'long_symbol': 'EU€',
        'symbol': '€',
        'title': 'Euro'
    }

    res = client.post('/v1/currencies', data=json.dumps(c), headers={
        'Content-Type': 'application/json'
    })
    assert res.status_code == 201
    d1 = json.loads(res.data)

    cpath = res.headers['Location']
    res = client.get(cpath)
    assert res.status_code == 200
    d2 = json.loads(res.data)

    for k, v in c.items():
        assert k in d1
        assert d1[k] == v
        assert k in d2
        assert d2[k] == v

def test_create_currency_bad_code(client):
    c = {
        'display_factor': 2,
        'iso4217_code': 'bAD',
        'long_symbol': 'EU€',
        'symbol': '€',
        'title': 'Euro'
    }

    res = client.post('/v1/currencies', data=json.dumps(c), headers={
        'Content-Type': 'application/json'
    })
    assert res.status_code == 400

def test_create_currency_no_symbol(client):
    c = {
        'display_factor': 2,
        'iso4217_code': 'EUR',
        'long_symbol': 'EU€',
        'title': 'Euro'
    }

    res = client.post('/v1/currencies', data=json.dumps(c), headers={
        'Content-Type': 'application/json'
    })
    assert res.status_code == 400

def test_create_currency_empty_symbol(client):
    c = {
        'display_factor': 2,
        'iso4217_code': 'EUR',
        'long_symbol': 'EU€',
        'symbol': '',
        'title': 'Euro'
    }

    res = client.post('/v1/currencies', data=json.dumps(c), headers={
        'Content-Type': 'application/json'
    })
    assert res.status_code == 400

def test_create_currency_long_symbol(client):
    c = {
        'display_factor': 2,
        'iso4217_code': 'EUR',
        'long_symbol': 'EU€',
        'symbol': 'LONG',
        'title': 'Euro'
    }

    res = client.post('/v1/currencies', data=json.dumps(c), headers={
        'Content-Type': 'application/json'
    })
    assert res.status_code == 400

def test_create_currency_no_code(client):
    c = {
        'display_factor': 2,
        'long_symbol': 'EU€',
        'symbol': '€',
        'title': 'Euro'
    }

    res = client.post('/v1/currencies', data=json.dumps(c), headers={
        'Content-Type': 'application/json'
    })
    assert res.status_code == 400

def test_create_currency_long_code(client):
    c = {
        'display_factor': 2,
        'iso4217_code': 'LONG',
        'long_symbol': 'EU€',
        'symbol': '€',
        'title': 'Euro'
    }

    res = client.post('/v1/currencies', data=json.dumps(c), headers={
        'Content-Type': 'application/json'
    })
    assert res.status_code == 400

def test_create_currency_no_title(client):
    c = {
        'display_factor': 2,
        'iso4217_code': 'EUR',
        'long_symbol': 'EU€',
        'symbol': '€'
    }

    res = client.post('/v1/currencies', data=json.dumps(c), headers={
        'Content-Type': 'application/json'
    })
    assert res.status_code == 400

def test_create_currency_empty_title(client):
    c = {
        'display_factor': 2,
        'iso4217_code': 'EUR',
        'long_symbol': 'EU€',
        'symbol': '€',
        'title': ''
    }

    res = client.post('/v1/currencies', data=json.dumps(c), headers={
        'Content-Type': 'application/json'
    })
    assert res.status_code == 400

def test_create_currency_empty_long_symbol(client):
    c = {
        'display_factor': 2,
        'iso4217_code': 'EUR',
        'long_symbol': '',
        'symbol': '€',
        'title': ''
    }

    res = client.post('/v1/currencies', data=json.dumps(c), headers={
        'Content-Type': 'application/json'
    })
    assert res.status_code == 400

def test_create_currency_long_long_symbol(client):
    c = {
        'display_factor': 2,
        'iso4217_code': 'EUR',
        'long_symbol': 'EEEEEEE',
        'symbol': '€',
        'title': ''
    }

    res = client.post('/v1/currencies', data=json.dumps(c), headers={
        'Content-Type': 'application/json'
    })
    assert res.status_code == 400

