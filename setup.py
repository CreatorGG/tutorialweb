#!/usr/bin/env python
# -*- coding:UTF-8 -*-

'''
Created on 2019年10月20日

@author: 肖炀  ( 广州大学 电子信息工程 2015级 )

summary:

'''

from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)