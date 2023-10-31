from flask import render_template, request, redirect, url_for, session, flash
from main import app, db, bcrypt
from functools import wraps
from main.forms import RegistrationForm, LoginForm
from main.models import User, Post, Task
from main.tests import *
from flask_login import login_user, current_user ,logout_user, login_required

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



@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html',title='register',form=form,current='home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user,remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
    return render_template('login.html',title='Login',form=form,current='home')


# User logout route
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

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


# acount rout
@app.route('/acount')
@login_required
def acount():
    return render_template('acount.html',current="count",title='Acount')

# error handler <page not found 404>
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404