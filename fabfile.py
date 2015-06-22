# encoding:utf8
__author__ = 'kongkongyzt'

from fabric.api import local

version_step = 0.1

def MtoR():
    local('pandoc -f markdown -t rst README.md > README.rst')

def localbuild():
    local('python setup.py bdist_egg')
    local('python setup.py sdist')

def pushToPip():
    local('python setup.py register')
    local('python setup.py sdist upload')

def upVersion():
    pass

def main():
    MtoR()
    localbuild()
    pushToPip()