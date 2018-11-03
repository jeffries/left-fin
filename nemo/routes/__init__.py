from flask import Blueprint, render_template

from nemo.routes.accounts import accounts_bp
import nemo.config

index_bp = Blueprint('index', __name__)

# If we are in development ONLY, proxy requests to /assets/* to localhost:5001
# This make it look like the frontend is served by the same server as the Python
# backend
if nemo.config.DEVELOPMENT:
    from requests import get
    from flask import Response

    @index_bp.route('/', methods=['GET'])
    def bootstrap():
        return render_template('bootstrap.html')

    @index_bp.route('/assets/<path:path>', methods=['GET'])
    def asset_forward(path):
        asset = get(f'http://localhost:5001/assets/{path}')
        return Response(
            asset.content,
            mimetype=asset.headers['Content-Type']
        )
