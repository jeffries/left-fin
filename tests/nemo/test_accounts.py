import json

import pytest

from nemo import app

@pytest.fixture
def client():
    c = app.test_client()
    yield c

def test_returns_object(client):
    """/v1/accounts returns an object"""

    r = client.get('/v1/accounts')
    assert 'accounts' in json.loads(r.data)