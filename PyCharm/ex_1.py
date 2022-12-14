#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit
from functools import lru_cache


def factorial_iter(n):
    product = 1
    while n > 1:
        product *= n
        n -= 1
    return product


def factorial_recurse(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial_recurse(n - 1)


@lru_cache
def factorial_rec_lru(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial_recurse(n - 1)


def fib_iter(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


def fib_recurse(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_recurse(n - 2) + fib_recurse(n - 1)


@lru_cache
def fib_rec_lru(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_rec_lru(n - 2) + fib_rec_lru(n - 1)


if __name__ == '__main__':
    print("*********** Time for factorial ***********")
    print("Time for iterative version:")
    print(f'{timeit.timeit(lambda: factorial_iter(50), number=10000)},\n')
    print("Time for recurse version:")
    print(f'{timeit.timeit(lambda: factorial_recurse(50), number=10000)},\n')
    print("Time for recurse_lru version:")
    print(f'{timeit.timeit(lambda: factorial_rec_lru(50), number=10000)},\n')
    print("*********** Time gor fib ***********")
    print("Time for iterative version:")
    print(f'{timeit.timeit(lambda: fib_iter(15), number=10000)},\n')
    print("Time for recurse version:")
    print(f'{timeit.timeit(lambda: fib_recurse(15), number=10000)},\n')
    print("Time for recurse_lru version:")
    print(timeit.timeit(lambda: fib_rec_lru(15), number=10000))
