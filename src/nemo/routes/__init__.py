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
    """Health check endpoint"""
    return "Hello World!"

# If we are in development mode, make the Python backend behave like a web server
# by forwarding requests to an instance of webpack-dev-server running on localhost:5001.
# We want this in development only to make the application work. In production, the
# content served in this section would be precompiled and served by a web server.
if nemo.config.DEVELOPMENT:
    LOGGER.warning('enabling asset serving pass-through for development')

    import re

    from requests import get
    from flask import Response # pylint: disable=ungrouped-imports

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

    # Serve bootstrap page on all paths to enable refreshing
    @INDEX_BP.route('/', methods=['GET'])
    @INDEX_BP.route('/<path:path>', methods=['GET'])
    def bootstrap(path=None):
        """Return a page to bootstrap the application"""
        LOGGER.info(path)
        if path and re.match('/assets/.*', path):
            raise ValueError()

        return render_template('bootstrap.html')
