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

def generalized_binomial_coefficient(n: int, np: int, m:int)->float: 
    if m > n + np:
        raise ValueError();
    kinf = ((m - n) + abs(m - n)) // 2
    ksup = min(m, np)
    s = 0.0
    for k in range(kinf, ksup + 1):
        s += (-1.0) ** k * binomial_coefficient(n, m - k) * binomial_coefficient(np, k)
    return s
