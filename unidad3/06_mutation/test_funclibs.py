import numpy as np
import pytest

import funclibs as gp


@pytest.mark.parametrize(
    "windows_size, h",
    [
        (1, [0.0, 0.0]),
        (2, [0.0, 1.0, 0.0]),
        (3, [0.0, 0.91830, 0.91830, 0.0]),
        (4, [0.0, 0.81127, 1.0, 0.81127, 0.0]),
        (5, [0.0, 0.72193, 0.97095, 0.97095, 0.72193, 0.0]),
        (6, [0.0, 0.65002, 0.91830, 1.0, 0.91830, 0.65002, 0.0]),
        (7, [0.0, 0.59167, 0.86312, 0.98522, 0.98522, 0.86312, 0.59167, 0.0]),
    ],
)
def test_risso_candidate_entropy(windows_size, h):
    me, _ = gp.risso_candidate_entropy(windows_size)
    assert np.allclose(me, h, atol=1e-05)


@pytest.mark.parametrize("windows_size", [0, -1])
def test_risso_candidate_entropy_le0(windows_size):
    with pytest.raises(ValueError):
        gp.risso_candidate_entropy(windows_size)


def test_argnearest():
    assert gp.argnearest([0.1, -0.98], 0) == 0
    assert gp.argnearest([0.1, -0.98], -0.99) == 1
    assert gp.argnearest([0.1, -0.10], 0.1) == 0


@pytest.mark.parametrize(
    "windows_size, sequence",
    [
        (1, [True]),
        (2, [False, True]),
        (3, [False, True, False]),
        (4, [False, True, False, True]),
        (5, [True, False, True, False, True]),
        (6, [True, False, True, False, True, False]),
        (7, [True, False, True, False, True, False, True]),
    ],
)
def test_loss_sequence(windows_size, sequence):
    result = gp.loss_sequence(
        loss_probability=0.33, windows_size=windows_size, seed=10
    )
    assert np.all(result == sequence)


def test_make_stock_price():
    assert gp.make_stock_price(100, True) < 100
    assert gp.make_stock_price(100, False) > 100



