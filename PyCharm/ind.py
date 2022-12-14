#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def matched(st, i, counter):
    if counter < 0:
        return "Недопустимая комбинация"
    while i < len(st):
        if st[i] == '(':
            counter += 1
            return matched(st, i + 1, counter)
        elif st[i] == ')':
            counter -= 1
            return matched(st, i + 1, counter)
        else:
            counter += 0
            return matched(st, i + 1, counter)
    if counter == 0:
        return "Ок"
    return "Недопустимая комбинация"


if __name__ == '__main__':
    s = input("Введите строку: ")
    print(matched(s, 0, 0))
