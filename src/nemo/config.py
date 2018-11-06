"""Configuration for nemo. These are all resolved when the application
comes up, and should not be changed subsequently."""

import os

# are we in development mode?
DEVELOPMENT = str(os.environ['FLASK_ENV']).upper() == 'DEVELOPMENT'

# are we in testing mode?
TESTING = str(os.environ['FLASK_ENV']).upper() == 'TESTING'

# database connection string
DB_STRING = str(os.environ['DB_STRING'])
