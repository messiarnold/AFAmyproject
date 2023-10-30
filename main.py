from functools import wraps
from datetime import datetime 
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import *
from forms import RegistrationForm, LoginForm

from tests import *


app = Flask(__name__)
app.config['SECRET_KEY'] = '84hfurh98fhwhe89ihds98yh93wh9dha8deh89weh9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(40),unique=True,nullable=False)
    password = db.Column(db.String(60),nullable=False)
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

# tasks menu you can add your tasks here 
tasks = {
    'task_1': {
        'title': 'Task 1',
        'test_function': evaluate_task_1,
        'instructions': 'Write code for Task 1: ...',
        'description' : "צעדים ראשונים בפייתון",
    },
    'task_2': {
        'title': 'Task 2',
        'test_function': evaluate_task_2,
        'instructions': 'Write code for Task 2: ...',
        'description' : "משתנים, קלט ופלט",
    },
    'task_2.1': {
        'title': 'Task 2.1',
        'test_function': evaluate_task_2_1,
        'instructions': 'Write code for Task 2.1: ...',
        'description' : "משתנים, קלט ופלט",
    },
    'task_2.2': {
        'title': 'Task 2.2',
        'test_function': evaluate_task_2_2,
        'instructions': 'Write code for Task 2.2: ...',
        'description' : "משתנים, קלט ופלט",
    },
    'task_2.3': {
        'title': 'Task 2.3',
        'test_function': evaluate_task_2_3,
        'instructions': 'Write code for Task 2.3: ...',
        'description' : "משתנים, קלט ופלט",
    },
    'task_2.4': {
        'title': 'Task 2.4',
        'test_function': evaluate_task_2_4,
        'instructions': 'Write code for Task 2.4: ...',
        'description' : "משתנים, קלט ופלט",
    },
    'task_13': {
        'title': 'Task 13',
        'test_function': evaluate_task_13,
        'instructions': 'Write code for Task 13: ...',
        'description' : "learn this also bla bla bla now!",
    },
    'task_3': {
        'title': 'Task 3',
        'test_function': evaluate_task_13,
        'instructions': 'Write code for Task 2: ...',
        'description' : "learn this also bla bla bla now!",
    },
    'task_12': {
        'title': 'Task 12',
        'test_function': evaluate_task_12,
        'instructions': 'Write code for Task 12: ...',
        'description' : "learn this bla bla bla now!",
    },
    # Define more tasks here
}

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))  # Redirect to login page if not logged in
    return decorated_function

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('login'))
    return render_template('register.html',title='register',form=form,current='home')
#def register():
#    if request.method == 'POST':
#        username = request.form['username']
#        password = request.form['password']
#        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
#
#        # Use a parameterized query to insert data
#        insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
#        data = (username, hashed_password)
#
#        cursor.execute(insert_query, data)
#        conn.commit()
#        
#        flash('Your account has been created! You can now log in.', 'success')
#        return redirect(url_for('login'))
#    return render_template('register.html')

# User login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html',title='Login',form=form,current='home')
#def login():
#    if request.method == 'POST':
#        username = request.form['username']
#        password = request.form['password']
#
#        # Use a parameterized query to fetch user data
#        select_query = "SELECT * FROM users WHERE username = %s"
#        data = (username,)
#        cursor.execute(select_query, data)
#        user = cursor.fetchone()
#
#        if user and bcrypt.check_password_hash(user[2], password):
#            session['logged_in'] = True
#            session['username'] = username 
#            return redirect(url_for('home'))
#        else:
#            flash('Login failed. Please check your credentials.', 'danger')
#
#    return render_template('login.html',current = "home")

# User logout route
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

# home route
@app.route("/")
@app.route('/home' )
def home():
    return render_template('home.html',current = "home")


# python content route
@app.route('/python')
def python():
    return render_template('python.html', current = "python",language = "python")


@app.route('/python/tasks', methods=['GET', 'POST'])
# @login_required in a comment for development issues
def tasks_page():
    return render_template('tasks.html',tasks=tasks,current = "python")


@app.route('/python/tasks/<task_name>', methods=['GET', 'POST'])
# @login_required in a comment for development issues
def task_page(task_name):
    task = tasks.get(task_name)
    if task is None:
        return "Task not found", 404
    if request.method == 'POST':
        code = request.form['code']
        feedback = task['test_function'](code)
        return render_template('task.html', task=task, code=code, feedback=feedback, task_progress=task_progress[task_name],current = "python")

    return render_template('task.html', task=task,task_progress=task_progress[task_name],current = "python")


# python videos route
@app.route('/python/videos')
def python_videos():
    return render_template('videos_python.html',current = "python")


# java route 
@app.route('/java')
def java():
    return render_template('java.html',current = "java",language="java")


# java videos route 
@app.route('/java/videos')
def java_videos():
    return render_template('videos_java.html',current = "java")


# about route
@app.route('/about')
def about():
    return render_template('about.html',current="about")


# error handler <page not found 404>
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


if __name__ == '__main__':
    app.run(debug=True)


