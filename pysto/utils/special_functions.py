#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scipy.special import factorial as fact
from scipy.special import factorial2 as fact2
from scipy.special import comb


def factorial(n: int) -> float:
    if n < 0:
        raise ValueError()
    return float(fact(n, exact=True))


def factorial2(n: int) -> float:
    if n < 0:
        raise ValueError()
    return float(fact2(n, exact=True))


def binomial_coefficient(n: int, k: int) -> float:
    if n < k:
        raise ValueError()
    return float(comb(n, k, exact=True))
