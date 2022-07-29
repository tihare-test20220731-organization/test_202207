import pytest
import numpy as np
from ttt.util import Util


@pytest.fixture
def lsh_integer():
    return np.array([1, 1, 1])


@pytest.fixture
def rsh_integer():
    return np.array([2, 3, 4])


def test_add(lsh_integer, rsh_integer):
    ans = np.array([3, 4, 5])
    assert np.allclose(Util.add(lsh_integer, rsh_integer), ans)


def test_sub(lsh_integer, rsh_integer):
    ans = np.array([-1, -2, -3])
    assert np.allclose(Util.sub(lsh_integer, rsh_integer), ans)


def test_sub_optional(rsh_integer):
    ans = np.array([-2, -3, -4])
    assert np.allclose(Util.sub(None, rsh_integer), ans)
