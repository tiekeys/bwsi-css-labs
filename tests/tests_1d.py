"""
tests_1d.py

This module contains unit tests for the two_sum function defined in lab_1d.py.
"""

import pytest
from labs.lab_1.lab_1d import two_sum

def test_one_case():
    assert two_sum([0, 1, 2, -4, 5], 6) == [1, 4]
    assert two_sum([9, 4, -3, 1, 2], 3) == [3, 4]

def test_two_case():
    assert two_sum([3, -2, 3, -4], 6) == [0, 2]
    assert two_sum([4, 2, -5, 1], 6) == [0, 1]

def test_no_case():
    assert two_sum([0, 5, 4], 1) == []
    assert two_sum([4, 5, -3, 12], 4) == []

if __name__ == "__main__":
    pytest.main()