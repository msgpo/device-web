from flask import Flask, session, redirect, url_for, escape, request, render_template
from datetime import timedelta
import pam

#https://github.com/jupyterlab/jupyterlab/blob/master/examples/app/main.py
# from jupyterlab_server import LabServerApp
# LabServerApp.launch_instance()


auth = pam.pam()

app = Flask(__name__)
app.secret_key = 'any random string x'

# app.permanent_session_lifetime = timedelta(minutes=1)


apps = [
    {'name': 'Music', 'url': '#', 'icon': 'music.svg'},
    {'name': 'Home Assistant', 'url': '#', 'icon': 'home_assistant.svg'},
    {'name': 'Google Assistant', 'url': '#', 'icon': 'google_assistant.svg'},
    {'name': 'Amazon Alexa', 'url': '#', 'icon': 'alexa.svg'}
]


@app.route('/')
def index():
    user = session['user'] if 'user' in session else None
    return render_template('index.html', user=user, apps=apps)

@app.route('/terminal')
def terminal():
    url = 'http://{0}/?src=terminal'.format(request.host)
    return redirect(url)

@app.route('/jupyter')
def jupyter():
    if 'user' not in session:
        return redirect(url_for('login', next='jupyter'))
    else:
        user = session['user']
        # todo: start jupyter-lab and navigate to it
        url = 'http://{0}/?src=jupyter'.format(request.host)
        return redirect(url)
    return render_template('login.html')

@app.route('/music')
def music():
    url = 'http://{0}/?src=music'.format(request.host)
    return redirect(url)


@app.route('/login', methods=['GET', 'POST'])
def login():
    print(request.args)
    print(request.method)
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        if auth.authenticate(user, password):
            session['user'] = request.form['user']
            session.permanent = True
            next = request.args['next'] if 'next' in request.args else 'index'
            return redirect(url_for(next))
        else:
            return render_template('login.html', message='Invalid username or password')

    return render_template('login.html')


@app.route('/logout')
def logout():
    # remove the user from the session if it is there
    session.pop('user', None)
    return redirect(url_for('index'))
