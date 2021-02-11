from flask import Flask, render_template, redirect, url_for, session, flash
from .forms import NameForm
from . import main

@main.route('/')
def index():
    return render_template('index.html', name_sent = session.get('name'))

@main.route('/user/<name>', methods = ['GET','POST'])
def user(name):
    div = 0.1
    value = 1/div
    achats = ['pomme', 'lait', 'cafe']

    user_name = None

    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        user_name = form.name.data
        form.name.data = ''

        if old_name is not None and old_name != user_name:
            flash("C'etait pas votre nom!")

        # Function to save in database...
        session['name'] = user_name
        return redirect(url_for('.index'))

    return render_template('name.html', nom=name, valeur=value, achats=achats, form=form, uname=session.get('name'))