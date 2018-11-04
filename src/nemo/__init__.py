# Configure logging
import logging

logging.basicConfig(level=logging.INFO) # TODO change depending on environment
logger = logging.getLogger(__name__)

# Initialize database
from nemo.models.db import init as db_init
# This import is important because it defines classes that db_init()
# uses to generate the CREATE TABLE statements
import nemo.models.schema

db_init()

# Create application
from flask import Flask
from nemo import config

app = Flask(__name__)
app.config.from_object(config)

# Register routes
import nemo.routes
app.register_blueprint(nemo.routes.index_bp)
app.register_blueprint(nemo.routes.accounts_bp)
