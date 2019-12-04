import pytest
from hello_world import *

#This is a test hello jenkins!

def test_hello():
    result = hello()
    assert result == "Hello!"
