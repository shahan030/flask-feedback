from database import db
from datetime import datetime

class Feedback(db.Model):
    __tablename__ = "feedback"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(120), nullable=False)  # using email as ID
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)   # remove unique constraint if multiple feedback allowed
    subject = db.Column(db.String(150), nullable=False) # new field for subject
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=True)
    sentiment = db.Column(db.String(20), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Feedback {self.id} - Rating: {self.rating}>"
