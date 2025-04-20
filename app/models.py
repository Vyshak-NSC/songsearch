from .extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    uid = db.Column(db.Integer, primary_key=True,autoincrement=True)
    username = db.Column(db.String(50) , nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    
    def set_password(self,password):
        self.password = generate_password_hash(password)
    
    def check_password(self,password):
        return check_password_hash(self.password,password)
        
    def get_id(self):
        return self.uid
    
    def __repr__(self):
        return f"<UID: {self.uid} User: {self.username}>"

class LikedSong(db.Model):
    sid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(400), nullable=False)
    author = db.Column(db.String(200))
