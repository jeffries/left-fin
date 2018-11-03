import os

DEVELOPMENT = str(os.environ['FLASK_ENV']).upper() == 'DEVELOPMENT'
