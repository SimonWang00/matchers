#!/usr/bin/python3
# __*__ coding: utf-8 __*__

'''
@Author: simonKing
@Os：Windows 10 x64
@Software: PY PyCharm
@File: setup.py
@Time: 2019/8/22 15:27
@Desc: setup.py
'''

from setuptools import setup


setup(
    name='matchers',
    version='0.1.0',
    url='https://github.com/SimonWang00/matchers',
    license='MIT',
    author='simon Wang',
    author_email='simon_wang00@163.com',
    description='Create the Best Universal Resolution Artifact',
    long_description=open('README.rst',encoding="utf-8").read() + '\n\n\n' + open('HISTORY.rst',encoding="utf-8").read(),
    include_package_data=True,
    install_requires=[
        'jieba',
        'bs4',
        "python-stdnum"
    ],
    packages=['matchers'],
    zip_safe=False,
    platforms='any',
    python_requires='>=3',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)

