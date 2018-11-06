import json

from util import client

def test_no_accounts(client):
    """/v1/accounts returns no accounts with an empty db"""

    res = client.get('/v1/accounts')

    assert res.status_code == 200
    data = json.loads(res.data)
    assert 'accounts' in data
    assert len(data['accounts']) == 0

def test_create_institution_account(client):
    """We can create an account and retrieve it"""

    a = {
        'type': 'institution_account',
        'title': 'Test Account',
        'institution_title': 'Test Trust',
        'number_suffix': '8770',
        'minimum_value': 0,
        'currency': 'USD'
    }

    res = client.post('/v1/accounts', data=json.dumps(a), headers={
        'Content-Type': 'application/json'
    })
    assert res.status_code == 201
    d1 = json.loads(res.data)
    assert 'id' in d1

    a_path = res.headers['Location']
    print(a_path)
    assert len(a_path) > 0
    res = client.get(a_path)
    assert res.status_code == 200
    d2 = json.loads(res.data)
    assert 'id' in d2

    for k, v in a.items():
        assert k in d1
        assert d1[k] == v
        assert k in d2
        assert d2[k] == v

def test_create_personal_account(client):
    """We can create an account and retrieve it"""

    a = {
        'type': 'personal_account',
        'holder': 'Jeffrey Lamar Williams',
        'currency': 'USD'
    }

    res = client.post('/v1/accounts', data=json.dumps(a), headers={
        'Content-Type': 'application/json'
    })
    assert res.status_code == 201
    d1 = json.loads(res.data)
    assert 'id' in d1

    a_path = res.headers['Location']
    print(a_path)
    assert len(a_path) > 0
    res = client.get(a_path)
    assert res.status_code == 200
    d2 = json.loads(res.data)
    assert 'id' in d2

    for k, v in a.items():
        assert k in d1
        assert d1[k] == v
        assert k in d2
        assert d2[k] == v


def test_create_invalid_institution_account(client):
    pass
