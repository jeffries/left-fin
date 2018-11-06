import os
import tempfile

import pytest

from nemo import app, models
from fixtures import init_fixtures

@pytest.fixture
def client():
    client = app.test_client()

    with models.db.session_scope() as session:
        # Empty all tables
        for table in reversed(models.db.BASE.metadata.sorted_tables):
            session.execute(table.delete())

        init_fixtures()

    yield client

def create_institution_account(title=None, institution_title=None, number_suffix=None, minimum_value=0, currency=None):
    pass
