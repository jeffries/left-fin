"""Module defining all route handlers for nemo"""

import logging

from flask import Blueprint, render_template

# Import blueprints from submodules so they are availabe in
# the module namespace
from nemo.routes.accounts import ACCOUNTS_BP
from nemo.routes.currencies import CURRENCIES_BP

import nemo.config

LOGGER = logging.getLogger(__name__)

INDEX_BP = Blueprint('index', __name__)

@INDEX_BP.route('/v1/hello', methods=['GET'])
def hello_world():
    return "Hello World!"

# If we are in development mode, make the Python backend behave like a web server
# We want this in development only to make the application work. In production, the
# content served in this section would be precompiled and served by a web server.
if nemo.config.DEVELOPMENT:
    LOGGER.warn('enabling asset serving pass-through for development')

    from requests import get
    from flask import Response

    # Serve bootstrap page
    @INDEX_BP.route('/', methods=['GET'], defaults={'path': None})
    @INDEX_BP.route('/<path:path>', methods=['GET'])
    def bootstrap():
        """Return a page to bootstrap the application"""
        return render_template('bootstrap.html')

    # Forward asset requests to localhost:5001
    # In the development Docker image, webpack-dev-server will be listening
    @INDEX_BP.route('/assets/<path:path>', methods=['GET'])
    def asset_forward(path):
        """Forward an asset request to webpack-dev-server in development"""
        asset = get(f'http://localhost:5001/assets/{path}', timeout=15)
        return Response(
            asset.content,
            mimetype=asset.headers['Content-Type']
        )
