from flask import Blueprint, render_template, jsonify

accounts_bp = Blueprint('accounts', __name__)

@accounts_bp.route('/accounts')
def list_accounts():
    return jsonify({
        'accounts': [
            {
                'id': 2
            }
        ]
    })
