from main import db, login_manager
from datetime import datetime 
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(40),unique=True,nullable=False)
    password = db.Column(db.String(60),nullable=False)
    is_teacher = db.Column(db.Integer,default=0)
    posts = db.relationship('Post',backref='author',lazy=False)
    tasks = db.relationship('Task',backref='author',lazy=False)
    
    def __repr__(self):
        return f'User("{self.username}", "{self.email}")'
    
class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(60),nullable=False)
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    content = db.Column(db.Text,nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f'User("{self.title}", "{self.date_posted}")'
    

class Task(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(60),nullable=False)
    attempts = db.Column(db.Integer,default=0)
    success = db.Column(db.Integer,default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f'User("{self.title}", "{self.attempts}")'