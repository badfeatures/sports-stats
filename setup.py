#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import
from setuptools import setup, find_packages, Command
import re
import os
import codecs

__title__ = 'Stats, LLC API Wrapper'
__version__ = '0.0.2'
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


with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

with open('requirements-dev.txt') as f:
    tests_require = f.read().splitlines()

print install_requires
print tests_require

setup(
    name='sportsstats',
    version=__version__,
    description='',
    url='https://github.com/sportsy/sports-stats',
    author=__author__,
    license=__license__,
    packages=find_packages(exclude=['tests.*', 'tests']),
    include_package_data=True,
    test_suite='nose.collector',
    install_requires=install_requires,
    dependency_links=['https://github.com/kennethreitz/requests/tarball/master#egg=requests==2.6.0'],
    tests_require=tests_require,
    cmdclass = {'test': PyTest},
    #entry_points={
    #     'console_scripts': [
    #         'sportsstats = sportsstats.api:main',
    #     ]
    # },
)