#4) Організувати безперервне введення чисел з клавіатури, поки користувач не введе 0.
#Після введення нуля, показати на екрані кількість чисел, які були введені,
#їх загальну суму і середнє арифметичне.

import re
def int_input(text):
    pattern = r"^\d+$"
    user_input = input(text)
    while not re.match(pattern, user_input):
        user_input = input("Введене значення некоректне, введіть натуральне число: ")
    return int(user_input)
def float_input(text):
    pattern2 = r"^-?\d+(\.\d+)?$"
    user_input = input(text)
    while not re.match(pattern2, user_input):
        user_input = input("Введене значення некоректне, введіть раціональне число: ")
    return float(user_input)

n=int_input("Введите n: ")
x=float_input("Введите x: ")
i=1
s=(x+i)/i
for i in range(1, n):
    s = s + (x+i)/i
print("s= ", s)