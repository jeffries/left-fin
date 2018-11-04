import json

import pytest

from nemo import app

@pytest.fixture
def client():
    c = app.test_client()
    yield c

def test_no_accounts(client):
    """/v1/accounts returns no accounts with an empty db"""

    res = client.get('/v1/accounts')
    assert res.status_code == 200
    data = json.loads(res.data)
    assert 'accounts' in data
    assert len(data['accounts']) == 0

def test_single_account(client):
    # We should mock an account in the database, and then
    # test that we can retrieve it

    # Force this test to fail for now
    assert False
