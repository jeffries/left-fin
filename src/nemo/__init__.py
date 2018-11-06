# Configure logging
import logging

from flask import Flask

from nemo.models.db import init as db_init
import nemo.models.schema
import nemo.routes
from nemo import config

logging.basicConfig(level=logging.INFO) # TODO change depending on environment

# Initialize database
db_init()

# Create application
app = Flask(__name__)
app.config.from_object(config)

# Register routes
app.register_blueprint(nemo.routes.INDEX_BP)
app.register_blueprint(nemo.routes.ACCOUNTS_BP)
app.register_blueprint(nemo.routes.CURRENCIES_BP)
