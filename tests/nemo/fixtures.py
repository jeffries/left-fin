from nemo.models.db import session_scope
from nemo.models.schema import Currency, Account, InstitutionAccount, PersonalAccount

def init_fixtures():
    c1 = Currency(
        title='United States Dollar',
        iso4217_code='USD',
        symbol='$',
        long_symbol='US$',
        display_factor=2
    )

    with session_scope() as s:
        s.add(c1)
