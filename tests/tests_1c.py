"""
tests_1c.py

This module contains unit tests for the simple_calculator function defined in lab_1b.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_max_subarray_sum():
    assert max_subarray_sum([4]) == 4
    assert max_subarray_sum([-1, 2, 5, -4, 3, -2, 1]) == 7
    assert max_subarray_sum([9, -9, 1, 0, 4, -3]) == 9

if __name__ == "__main__":
    pytest.main()