#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit
import sys


class TailRecurseException(Exception):
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs


def tail_call_optimized(g):
    # Эта программа показывает работу декоратора, который производит оптимизацию
    # хвостового вызова. Он делает это, вызывая исключение, если оно является его
    # прародителем, и перехватывает исключения, чтобы подделать оптимизацию хвоста.
    # Эта функция не работает, если функция декоратора не использует хвостовой вызов.

    def func(*args, **kwargs):
        f = sys._getframe()
        if f.f_back and f.f_back.f_back and f.f_back.f_back.f_code == f.f_code:
            raise TailRecurseException(args, kwargs)
        else:
            while True:
                try:
                    return g(*args, **kwargs)
                except TailRecurseException as e:
                    args = e.args
                    kwargs = e.kwargs

    func.__doc__ = g.__doc__
    return func


def factorial(n, acc=1):
    if n == 0:
        return acc
    return factorial(n - 1, n * acc)


def fib_recurse(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_recurse(n - 2) + fib_recurse(n - 1)


@tail_call_optimized
def factorial_opt(n, acc=1):
    if n == 0:
        return acc

    return factorial(n - 1, n * acc)


@tail_call_optimized
def fib_opt(i, current=0, next=1):
    if i == 0:
        return current
    else:
        return fib_opt(i - 1, next, current + next)


if __name__ == '__main__':
    print("*********** Time for factorial ***********")
    print("Время работы кода без использования интроспекции:")
    print(f'{timeit.timeit(lambda: factorial(500), number=10000)}\n')
    print("Время работы кода с использованием интроспекции:")
    print(f'{timeit.timeit(lambda: factorial_opt(500), number=10000)}\n')
    print("*********** Time gor fib ***********")
    print("Время работы кода без использования интроспекции:")
    print(timeit.timeit(lambda: fib_recurse(15), number=10000))
    print("Время работы кода с использованием интроспекции:")
    print(f'{timeit.timeit(lambda: fib_opt(15), number=10000)}\n')
