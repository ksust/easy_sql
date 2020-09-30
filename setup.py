#!/usr/bin/env python
# -*-coding:utf-8-*-
from setuptools import setup, find_packages

setup(
    name='easy_sql',
    version='0.0.2',
    description=
    'easy to use mysql(kb)',
    long_description=open('README.rst', encoding='utf-8').read(),
    author='ksust',
    author_email='admin@ksust.com',
    maintainer='ksust',
    maintainer_email='admin@ksust.com',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/ksust/easy_sql',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[
        'SQLAlchemy==1.3.13',
        'PyYAML==5.3.1',
    ]
)