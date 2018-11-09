"""Main module for nemo backend. The `app` member will be detected by Flask
when we run `flask run`"""

import nemo.config

# Configure logging before anything else
import logging
if nemo.config.DEVELOPMENT or nemo.config.TESTING:
    logging.basicConfig(level=logging.INFO)

from flask import Flask # pylint: disable=wrong-import-position

from nemo.models.db import init as db_init # pylint: disable=wrong-import-position,ungrouped-imports
import nemo.models.schema # pylint: disable=wrong-import-position,ungrouped-imports
import nemo.routes # pylint: disable=wrong-import-position,ungrouped-imports

# Initialize database
db_init()

# Create and configure application
app = Flask(__name__) # pylint: disable=invalid-name
app.config.from_object(nemo.config)

# Register routes
app.register_blueprint(nemo.routes.INDEX_BP)
app.register_blueprint(nemo.routes.ACCOUNTS_BP)
app.register_blueprint(nemo.routes.CURRENCIES_BP)
