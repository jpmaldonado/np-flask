from flask import Flask, render_template, redirect, url_for, session, flash
from ..models import User, Role
from .. import db
from .forms import NameForm
from . import main

@main.route('/')
def index():
    return render_template('index.html', name_sent = session.get('name'))

def decode_role(role):
    return 1 if role == 'Admin' else 2

@main.route('/user/create', methods = ['GET','POST'])
def create_user():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data, role_id=decode_role(form.role.data))
            db.session.add(user)
            db.session.commit() 
        flash("User saved!")
        return redirect(url_for('.index'))

    return render_template('create_user.html', form=form)

@main.route('/user/view')
def view_users():
    users_roles = User.query.join(Role, Role.id==User.role_id).all()
    #print(users_roles) #this is where __repr__ is useful :D
    return render_template('users.html', users = users_roles)    