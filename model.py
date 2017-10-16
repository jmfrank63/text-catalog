#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
The database model
'''
from app import db

class Language(db.Model):
    '''
    This table stores the language name
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    def __init__(self, name):
        '''
        Init the language class with a name
        '''
        self.name = name

    def __unicode__(self):
        '''
        Print a nice representation of the language object
        '''
        return "Language(Id={}, name={})".format(self.id, self.name)


class User(db.Model):
    '''
    This table stores the user information
    username and email
    '''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)

    def __init__(self, username, email):
        '''
        Init the User with a username and an email address
        '''
        self.username = username
        self.email = email

    def __unicode__(self):
        '''
        Print a nice representaio of the the user object
        '''
        return "User(Id={}, username={}, email={})".format(self.id,
                                                           self.username,
                                                           self.email)


class Sentence(db.Model):
    '''
    This table stores the sentence information
    '''
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    translation = db.Column(db.String, nullable=False)
    language_id = db.Column(db.Integer, db.ForeignKey('language.id'))
    language = db.relationship('Language',
        backref=db.backref('sentences', lazy='dynamic'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User',
        backref=db.backref('sentences', lazy='dynamic'))

    def __init__(self, text, translation, language, user):
        '''
        Init the sentence with text, translation, language and user
        '''
        self.text = text
        self.translation = translation
        self.language = language
        self.user = user

    def __unicode__(self):
        '''
        Print a nice representation of the Sentence object
        '''
        return "Sentence(Id={}, text={}, translation={}, language={},user={})"\
            .format(self.id,
                    self.text,
                    self.translation,
                    self.language,
                    self.user)
