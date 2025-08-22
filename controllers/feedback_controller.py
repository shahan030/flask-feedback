from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity
from models.feedback import Feedback
from database import db
from datetime import datetime

def create_feedback():
    data = request.get_json()
    if not data:
        return jsonify({"msg": "Request body is required"}), 400

    
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({"msg": "User not found"}), 401

    user_email = current_user.get("email")
    roles = current_user.get("additional_claims", {}).get("role", [])

   
    if "User" not in roles:
        return jsonify({"msg": "Insufficient role"}), 403

   
    name = data.get("name", "").strip()
    subject = data.get("subject", "").strip()
    comment = data.get("comment", "").strip()
    rating = data.get("rating")

    if not name or not isinstance(name, str):
        return jsonify({"msg": "Name must be a string"}), 400
    if not subject or not isinstance(subject, str):
        return jsonify({"msg": "Subject must be a string"}), 400
    if not comment or not isinstance(comment, str):
        return jsonify({"msg": "Comment must be a string"}), 400

    try:
        rating = int(rating)
    except (TypeError, ValueError):
        return jsonify({"msg": "Rating must be an integer between 1 and 5"}), 400
    if not (1 <= rating <= 5):
        return jsonify({"msg": "Rating must be between 1 and 5"}), 400

   
    feedback = Feedback(
        user_id=user_email,  # use email as ID
        name=name,
        email=user_email,
        subject=subject,
        comment=comment,
        rating=rating,
        created_at=datetime.utcnow()
    )

    try:
        db.session.add(feedback)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": f"Database error: {str(e)}"}), 500

    return jsonify({"msg": "Feedback submitted successfully"}), 201
