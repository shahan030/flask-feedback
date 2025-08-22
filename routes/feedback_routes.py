from flask import Blueprint
from controllers.feedback_controller import create_feedback
from flask_jwt_extended import jwt_required

feedback_bp = Blueprint("feedback_bp", __name__)

@feedback_bp.route("/feedback", methods=["POST"])
@jwt_required()
def feedback_route():
    return create_feedback()
