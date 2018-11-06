import os
import tempfile

import pytest

from nemo import app, models
from fixtures import init_fixtures

@pytest.fixture
def client():
    c = app.test_client()

    with models.db.session_scope() as session:
        # Empty all tables
        for table in reversed(models.db.Base.metadata.sorted_tables):
            session.execute(table.delete())

        init_fixtures()

    yield c

def create_institution_account(title=None, institution_title=None, number_suffix=None, minimum_value=0, currency=None):
    pass
