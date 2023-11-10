from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from main import db, login_manager, app
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
    
    def get_reset_token(self,expires_sec=1200):
        s = Serializer(app.config['SECRET_KEY'],expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')
    
    @staticmethod
    def verify_reset_token(token):
            s = Serializer(app.config['SECRET_KEY'])
            try:
                user_id = s.loads(token)['user_id']
            except:
                return None
            return User.query.get(user_id)
        
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