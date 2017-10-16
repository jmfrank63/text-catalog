#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Text catalog application
'''
from app import app, db
from model import Language, User, Sentence
from flask import render_template, url_for, redirect
import os


@app.route('/')
def index():
    ''' The start page '''
    return render_template('index.html')

@app.route('/login')
def login():
    ''' Handles the user login '''
    return "This will be the login page"
    
@app.route('/languages')
def languages():
    ''' Gives an overview of all languages '''
    return "This will be the language overview page"
    
@app.route('/language/<int:lid>')
def language(lid):
    ''' Shows the content of a language '''
    return "This will show the content of a language {0}".format(lid)
    
@app.route('/language/<int:lid>/sentence/<int:sid>')
def sentence(lid, sid):
    ''' Shows the content of a sentence '''
    return "This will show the content of sentence {1} of language {0}".format(lid, sid)
    

@app.route('/db/')
def database():
    '''
    Dumps the database out on one page
    '''
    languages = Language.query.all()
    users = User.query.all()
    sentences = Sentence.query.all()
    return render_template('database.html', users=users, 
                                         languages=languages,
                                         sentences=sentences)

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'),
            port=int(os.getenv('PORT', 8080)),
            debug=True)