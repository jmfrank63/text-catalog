#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Text catalog application
'''
from const import DB_FILE
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


def create_app():
    ''' Create the flask app and its extensions '''
    app = Flask(__name__)
    Bootstrap(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/ubuntu/workspace/' + DB_FILE
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    return app, db
    
app, db = create_app()
