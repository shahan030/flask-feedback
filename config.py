import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_D=os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(BASE_D,'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY=os.getenv("JWT_KEY")