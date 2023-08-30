from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user

from todo_app import app, login, db
from .forms import UserForm, TaskForm
from .models import User, Task


@app.route('/', methods=['GET', 'POST'])
def mainpage():  # put application's code here
    form = TaskForm()
    if current_user.is_authenticated:
        tasks = Task.query.filter_by(user_id=current_user.id)
    else:
        tasks = None
    if form.validate_on_submit():
        task = Task(task=form.task.data, expire_date=form.expire_date.data, user_id=current_user.id)
        db.session.add(task)
        db.session.commit()
        flash('Task succesfully added!')
        return redirect(url_for('mainpage'))
    return render_template('index.html', form=form, tasks=tasks)


@app.route('/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Task succesfully deleted!')
    return redirect(url_for('mainpage'))


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('mainpage'))
    form = UserForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('mainpage'))
    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('mainpage'))
    form = UserForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You are registered now!')
        return redirect(url_for('mainpage'))
    return render_template('signup.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('mainpage'))
