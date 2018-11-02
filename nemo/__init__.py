# Configure logging
import logging

logging.basicConfig(level=logging.INFO) # TODO change depending on environment
logger = logging.getLogger(__name__)

# Initialize database
from nemo.models.db import init as db_init
import nemo.models.schema

db_init()

# Create application
from flask import Flask
from nemo import config

app = Flask(__name__)
app.config.from_object(config)

# Register views
import nemo.views
app.register_blueprint(nemo.views.index_bp)
