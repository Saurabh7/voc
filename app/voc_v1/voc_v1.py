# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, jsonify

# Define the blueprint: 'auth', set its url prefix: app.url/auth
voc_v1 = Blueprint('voc_v1', __name__, url_prefix='/voc_v1')

# Set the route and accepted methods
@voc_v1 .route('/voc_v1/', methods=['POST'])
def voc_v1_data():
    data = request.get_json()
    return jsonify(data)