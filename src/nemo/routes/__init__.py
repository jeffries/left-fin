import logging

from flask import Blueprint, render_template

# Import blueprints from submodules so they are availabe in
# the module namespace
from nemo.routes.accounts import accounts_bp
from nemo.routes.currencies import currencies_bp

import nemo.config

logger = logging.getLogger(__name__)

index_bp = Blueprint('index', __name__)

@index_bp.route('/v1/hello', methods=['GET'])
def hello_world():
    return "Hello World!"

# If we are in development mode, make the Python backend behave like a web server
# We want this in development only to make the application work. In production, the
# content served in this section would be precompiled and served by a web server.
if nemo.config.DEVELOPMENT:
    logger.warn('enabling asset serving pass-through for development')

    from requests import get
    from flask import Response

    # Serve bootstrap page
    @index_bp.route('/', methods=['GET'], defaults={'path': None})
    @index_bp.route('/<path:path>', methods=['GET'])
    def bootstrap(path):
        return render_template('bootstrap.html')

    # Forward asset requests to localhost:5001
    # In the development Docker image, webpack-dev-server will be listening
    @index_bp.route('/assets/<path:path>', methods=['GET'])
    def asset_forward(path):
        asset = get(f'http://localhost:5001/assets/{path}', timeout=15)
        return Response(
            asset.content,
            mimetype=asset.headers['Content-Type']
        )
