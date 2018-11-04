from sqlalchemy import Column, Integer, String, ForeignKey, Date, DateTime, LargeBinary
from sqlalchemy.orm import relationship, column_property

from nemo.models.db import Base

class Currency(Base):
    __tablename__ = 'currencies'

    iso4217_code = Column(String(3), primary_key=True)
    title = Column(String)
    symbol = Column(String(1))
    long_symbol = Column(String(3))

    accounts = relationship('Account', back_populates='currency')

class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    currency_code = Column(String(3), ForeignKey('currencies.iso4217_code'))
    type = Column(String(255))

    currency = relationship('Currency', back_populates='accounts')

    __mapper_args__ = {
        'polymorphic_identity': 'account',
        'polymorphic_on': type
    }

class InstitutionAccount(Base):
    __tablename__ = 'institution_accounts'

    id = Column(Integer, ForeignKey('accounts.id'), primary_key=True)
    title = Column(String(255))
    number_suffix = Column(String(4))
    institution_title = Column(String(255))
    minimum_value = Column(Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'institution_account'
    }

class PersonalAccount(Base):
    __tablename__ = 'personal_accounts'

    id = Column(Integer, ForeignKey('accounts.id'), primary_key=True)
    holder = Column(String(255))

    __mapper_args__ = {
        'polymorphic_identity': 'personal_account'
    }

class TransactionCategory(Base):
    __tablename__ = 'transaction_categories'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    parent = Column(Integer, ForeignKey('transaction_categories.id'))

class AccountTransaction(Base):
    __tablename__ = 'account_transactions'

    id = Column(Integer, primary_key=True)
    account = Column(Integer, ForeignKey('accounts.id'))
    title = Column(String(255))
    transaction_date = Column(Date)
    posting_date = Column(Date)
    merchant = Column(String(255))
    transaction_amount = Column(Integer)
    gain_or_loss = Column(Integer)
    instrument = Column(String(255))
    transaction_description = Column(String)
    adjustment_description = Column(String)

class TransactionAdjustment(Base):
    __tablename__ = 'transaction_adjustments'

    id = Column(Integer, primary_key=True)
    source_transaction_id = Column(Integer, ForeignKey('account_transactions.id'))
    destination_transaction_id = Column(Integer, ForeignKey('account_transactions.id'))
    title = Column(String(255))
    notes = Column(String)
    type = Column(String(255))

    __mapper_args__ = {
        'polymorphic_identity': 'transaction_adjustment',
        'polymorphic_on': type
    }


class AccountTransactionAdjustment(Base):
    __tablename__ = 'account_transaction_adjustments'

    id = Column(Integer, ForeignKey('transaction_adjustments.id'), primary_key=True)
    amount = Column(Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'account_transaction_adjustment'
    }

class CurrencyConversionAdjustment(Base):
    __tablename__ = 'currency_conversion_adjustment'

    id = Column(Integer, ForeignKey('transaction_adjustments.id'), primary_key=True)
    source_amount = Column(Integer)
    destination_amount = Column(Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'currency_conversion_adjustment'
    }


class TransactionCategorization(Base):
    __tablename__ = 'transaction_categorizations'

    transaction_id = Column(Integer, ForeignKey('account_transactions.id'), primary_key=True)
    category_id = Column(Integer, ForeignKey('transaction_categories.id'), primary_key=True)
    amount = Column(Integer)
    notes = Column(String)

class Receipt(Base):
    __tablename__ = 'receipts'

    id = Column(Integer, primary_key=True)
    transaction_id = Column(Integer, ForeignKey('account_transactions.id'))
    image_jpeg = Column(LargeBinary)
    image_pdf = Column(LargeBinary)
    notes = Column(String)

class BudgetCategory(Base):
    __tablename__ = 'budget_categories'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    parent = Column(Integer, ForeignKey('budget_categories.id'))

class Budget(Base):
    __tablename__ = 'budgets'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    currency = Column(String(3), ForeignKey('currencies.iso4217_code'))

class BudgetItem(Base):
    __tablename__ = 'budget_items'

    id = Column(Integer, primary_key=True)
    budget_id = Column(Integer, ForeignKey('budgets.id'))
    category_id = Column(Integer, ForeignKey('budget_categories.id'))
    title = Column(String(255))
    notes = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    amount = Column(Integer)
