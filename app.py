#!/usr/bin/env python
from flask import Flask, Response
from flask.ext.sqlalchemy import SQLAlchemy
from os.path import abspath, join, dirname

DB_PATH = abspath(join(dirname(__file__), 'migrations', 'project.db'))
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////{}'.format(DB_PATH)
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(128), unique=True)


@app.route('/add/<username>/')
def root(username):
    print username
    user = User(username=username, email='test@mattjmorrison.com')
    db.session.add(user)
    db.session.commit()
    return Response('<br />'.join([u.username for u in User.query.all()]))


@app.route('/favicon.ico')
def favicon():
    return Response("")


if __name__ == '__main__':
    app.run()
