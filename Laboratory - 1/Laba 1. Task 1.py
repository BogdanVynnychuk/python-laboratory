#Користувач уводить три числа.
#Збільшити перше число в два рази,
#друге числа зменшити на 3,
#третє число звести в квадрат і потім знайти суму нових трьох чисел.
import re
def float_input(text):
    pattern = "^-?\d+(\.\d+)?$"
    user_input = input(text)
    while not re.match(pattern, user_input):
        user_input = input("Введене значення некоректне , Введіть число:")
    return float(user_input)
a= float_input("Введите число а ")
b= float_input("Введите число b ")
c= float_input("Введите число c ")
a=a*2
b=b-3
c=c**2
s=a+b+c
print("Сума чисел:", s)