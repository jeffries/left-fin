"""Magic numbers (constants) for use by the models package."""

# Table names
CURRENCY_TABLE = 'currencies'
ACCOUNT_TABLE = 'accounts'
INSTITUTION_ACCOUNT_TABLE = 'institution_accounts'
PERSONAL_ACCOUNT_TABLE = 'personal_accounts'
TRANSACTION_CATEGORY_TABLE = 'transaction_categories'
ACCOUNT_TRANSACTION_TABLE = 'account_transactions'
TRANSACTION_ADJUSTMENT_TABLE = 'transaction_adjustments'
ACCOUNT_TRANSACTION_ADJUSTMENT_TABLE = 'account_transaction_adjustments'
CURRENCY_CONVERSION_ADJUSTMENT_TABLE = 'currency_conversion_adjustment'
TRANSACTION_CATEGORIZATION_TABLE = 'transaction_categorizations'
RECEIPT_TABLE = 'receipts'
BUDGET_CATEGORY_TABLE = 'budget_categories'
BUDGET_TABLE = 'budgets'
BUDGET_ITEM_TABLE = 'budget_items'

# Polymorphic identities
ACCOUNT_POLYID = 'account'
INSTITUTION_ACCOUNT_POLYID = 'institution_account'
PERSONAL_ACCOUNT_POLYID = 'personal_account'
CURRENCY_CONVERSION_ADJUSTMENT_POLYID = 'currency_conversion_adjustment'
ACCOUNT_TRANSACTION_ADJUSTMENT_POLYID = 'account_transaction_adjustment'
TRANSACTION_ADJUSTMENT_POLYID = 'transaction_adjustment'
