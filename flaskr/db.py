#!/usr/bin/env python
# -*- coding:UTF-8 -*-

'''
Created on 2019年10月18日

@author: 肖炀  ( 广州大学 电子信息工程 2015级 )

summary:

'''

import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()