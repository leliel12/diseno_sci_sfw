#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 15:09:17 2021

@author: nadia
"""


import numpy as np
import pandas as pd

_ENT = -1 / np.log2(2)


def risso_candidate_entropy(windows_size):
    if windows_size <= 0:
        raise ValueError("'windows_size' must be > 0")

    loss_probability = np.linspace(0.0, 1.0, num=windows_size + 1)

    # Se corrigen probabilidades porque el cálculo de la entropía trabaja con
    # logaritmo y el logaritmo de cero no puede calcularse
    epsilon = np.finfo(loss_probability.dtype).eps
    loss_probability[0] = epsilon
    loss_probability[-1] = 1 - epsilon

    # Calcula entropy
    first_part = loss_probability * np.log2(loss_probability)
    second_part = (1 - loss_probability) * np.log2(1 - loss_probability)

    modificated_entropy = _ENT * (first_part + second_part)
    return modificated_entropy, loss_probability


def argnearest(arr, v):
    diff = np.abs(np.subtract(arr, v))
    idx = np.argmin(diff)
    return idx


def loss_sequence(windows_size, loss_probability, seed=None):
    random = np.random.default_rng(seed=seed)
    probability_win = 1 - loss_probability
    sequence = random.choice(
        [True, False], size=windows_size, p=[loss_probability, probability_win]
    )
    if random.choice([True, False]):
        sequence = ~sequence
    return sequence


def make_stock_price(price, loss, seed=None):
    if price == 0. :
        return 0.
    random = np.random.default_rng(seed=seed)
    sign = -1 if loss else 1
    day_return = sign * np.abs(random.normal(0, 1))
    new_price = price + day_return
    return 0. if new_price < 0 else new_price

