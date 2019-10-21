#!/usr/bin/env python
# -*- coding:UTF-8 -*-

'''
Created on 2019-10-21

@author: 肖炀  ( 广州大学 电子信息工程 2015级 )

summary:

'''

from flaskr import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'