from flask import Blueprint, render_template, jsonify

accounts_bp = Blueprint('accounts', __name__)

@accounts_bp.route('/v1/accounts', methods=['GET'])
def list_accounts():
    accounts = []

    return jsonify({
        'accounts': accounts
    })
