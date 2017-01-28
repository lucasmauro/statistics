# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='statstuff',
    version='0.0.3',
    description='Statistics calculator',
    long_description=readme,
    author='Lucas Mauro',
    author_email='hello@lucasmauro.net',
    url='https://github.com/lucasmauro/statstuff',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)