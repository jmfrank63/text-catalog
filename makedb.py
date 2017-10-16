#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Create a new database 
'''
from const import DB_FILE
from app import db
from model import *
import os


def main():
    '''
    Create create a backup a new database
    '''
    if os.path.isfile(DB_FILE):
        if os.path.isfile(DB_FILE + '.bak'):
            os.remove(DB_FILE + '.bak')
        os.rename(DB_FILE, DB_FILE + '.bak')
    db.create_all()
    
if __name__ == '__main__':
    main()    
