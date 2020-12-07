#!/usr/bin/env python

from setuptools import find_packages
from setuptools import setup

#PROJECT = 'cliffdemo'
PROJECT = 'dailycheck'

# Change docs/sphinx/conf.py too!
VERSION = '0.1'

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''

setup(
    name=PROJECT,
    version=VERSION,

    description='DailyCheck app based on cliff',
    long_description=long_description,

    author='Chang4Tech',
    author_email='chang4tech@gmail.com',

    url='https://github.com/chang4tech/dailycheck',
    download_url='',

    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.2',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 ],

    platforms=['Any'],

    scripts=[],

    provides=[],
    install_requires=['cliff'],

    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'dailycheck = dailycheck.main:main',
        ],
	'dailycheck.demo': [
        'init = dailycheck.init:Init',
        'add = dailycheck.add:Add',
        'remove = dailycheck.remove:Remove',
        'check = dailycheck.check:Check',
        'greeting = dailycheck.greeting:Greeting',
        'show = dailycheck.show:Show', 
	],
    },

    zip_safe=False,
)
