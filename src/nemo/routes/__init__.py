from flask import Blueprint, render_template

# Import blueprints from submodules so they are availabe in
# the module namespace
from nemo.routes.accounts import accounts_bp

import nemo.config

index_bp = Blueprint('index', __name__)

# If we are in development mode, make the Python backend behave like a web server
if nemo.config.DEVELOPMENT:
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
        asset = get(f'http://localhost:5001/assets/{path}')
        return Response(
            asset.content,
            mimetype=asset.headers['Content-Type']
        )
