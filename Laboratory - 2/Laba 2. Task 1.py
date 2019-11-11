#4)	Обчислити суму

import re
import sys


def int_input(text):
    pattern = r"^[-\d]\d*$"
    user_input = input(text)
    while not re.match(pattern, user_input):
        user_input = input("Введене значення некоректне, введіть ціле число:")
    return int(user_input)


def float_input(text):
    pattern = r"^-?\d+(\.\d+)?$"
    user_input = input(text)
    while not re.match(pattern, user_input):         user_input = input(
    "Введене значення некоректне, введіть раціональне число:")
    return float(user_input)

def funct():
    n = int_input("Введіть n: ")
    x = float_input("Введіть x: ")
    s = 0
    for i in range(1, n + 1):
        s += (x + i) / i
        print("s=", s)
    q = int_input("Ввести значення повторно? 1 - так, 0 - завершити програму ")
    if q == 1:
        funct()
    elif q == 0:
        sys.exit(0)
    else:
        print("Введіть значення 1 або 0")

funct()

