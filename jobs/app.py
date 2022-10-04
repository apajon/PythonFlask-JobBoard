import flask
from flask import render_template

app = flask(__name__)

@route('/')
@route('/jobs')
def jobs():
    return render_template('index.html')

