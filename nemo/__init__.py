import logging

logging.basicConfig(level=logging.INFO) # TODO change depending on environment

logger = logging.getLogger(__name__)

from flask import Flask, render_template

from nemo import config

app = Flask(__name__)

from nemo.models.db import init as db_init
import nemo.models.schema

db_init()

import nemo.views

app.register_blueprint(nemo.views.index_bp)
