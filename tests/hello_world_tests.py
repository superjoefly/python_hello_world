from nose.tools import *
import hello_world

def setup():
    print 'SETUP!'

def teardown():
    print 'TEAR DOWN!'

def test_basic():
    print 'I RAN!'
