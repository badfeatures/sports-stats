#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import
from setuptools import setup, find_packages, Command
import re
import os
import codecs

__title__ = 'Stats, LLC API Wrapper'
__version__ = '0.0.1'
__author__ = 'Sportsy, Inc.'
__license__ = 'MIT'
__copyright__ = 'Copyright 2015 Sportsy, Inc.'



class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import subprocess
        import sys
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)

def read(*parts):
    path = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(path, encoding='utf-8') as fobj:
        return fobj.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

def get_readme():
    try:
        with open('README.rst') as f:
            return f.read().strip()
    except IOError:
        return ''


with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

with open('requirements-dev.txt') as f:
    tests_require = f.read().splitlines()

setup(
    name='sports-stats',
    version=__version__,
    description='',
    long_description=get_readme(),
    author=__author__,
    url='https://github.com/sportsy/sports-stats',
    packages=['sportsstats'],
    package_data={
        'sportsstats': [__version__]
    },
    install_requires=install_requires,
    dependency_links=['https://github.com/kennethreitz/requests/tarball/master#egg=requests==2.6.0'],
    test_suite='nose.collector',
    tests_require=tests_require,
    cmdclass = {'test': PyTest},
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
     ],
)