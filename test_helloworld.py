import pytest
from Hello_World import *

#This is a test hello jenkins!

def test_hello():
    result = hello()
    assert result == "Hello!"
