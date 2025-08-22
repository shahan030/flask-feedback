from database import db
import hashlib

class User(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(80),nullable=False,unique=True)
    email=db.Column(db.String(70),nullable=False,unique=True)
    password=db.Column(db.String(120),nullable=False,)


    def __init__(self,username,password,email) :
        self.username =username
        self.email =email
        self.password = hashlib.sha256(password.encode()).hexdigest()
