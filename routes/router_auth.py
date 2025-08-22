from flask import Blueprint
from controllers import auth_Controller

auth_bp = Blueprint('auth_bp',__name__)
# register
auth_bp.route("/register",methods=["POST"])(auth_Controller.signUp)

# login
auth_bp.route("/login",methods=["POST"])(auth_Controller.signIn)