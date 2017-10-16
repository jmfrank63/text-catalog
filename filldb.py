#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Create the database content
'''
from const import SENTENCE_FILE, USER_FILE
from app import db
from model import *
import csv
import random

def tprint(obj):
    print repr(obj).decode('unicode-escape').encode('latin-1')
    
def main():
    '''
    Fill the database
    '''
    with open(USER_FILE) as userfile:
        user_reader = csv.DictReader(userfile, delimiter=';')
        users = [User(unicode(user['Username'],'utf8'), 
                      unicode(user['Email'],'utf8')) 
                 for user in user_reader]
        db.session.add_all(users)
        db.session.commit()
        
    with open(SENTENCE_FILE) as langfile:
        lang_reader = csv.DictReader(langfile, delimiter='\t')
        languages = [Language(unicode(name, 'utf8')) for name in lang_reader.fieldnames]
        db.session.add_all(languages)
        db.session.commit()
        for sentences in lang_reader:
            text = unicode(sentences['English'],'utf8')
            for lang_name, translation in sentences.iteritems():
                user = User.query.get(random.randint(1,40))
                language = Language.query.filter_by(name=lang_name).one()
                sentence = Sentence(text, unicode(translation,'utf8'), language, user)
                db.session.add(sentence)
                db.session.commit()
        
if __name__ == '__main__':
    import makedb
    makedb.main()
    main()

    