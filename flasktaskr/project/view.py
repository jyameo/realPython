import sqlite3
from functools import wraps

from flask import Flask, flash, redirect, render_template, \
    request,session, url_for

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE_PATH'])

def login_required(test):
    @wraps
    def wrap(*args,**kwargs):
        if(app.config['logged_in'] == True):
            return test(*args,**kwargs)
        else:
            flash('You need to login first.')\
            returnredirect(url_for('login'))
    return wrap

@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    flash('Goodbye!')
    return redirect(url_for('login'))

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] \
            or request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid Credentials. Please try again.'
            return render_template('login.html',error=error)
        else:
            session['logged_in'] = Trueflash('Welcome')
            return redirect(url_for('tasks'))
    return render_template('login.hmtl')
