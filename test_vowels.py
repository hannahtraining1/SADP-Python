import pytest
from applications import vowels

def test_are_vowels():
    assert vowels.vowels("hello world") == 3