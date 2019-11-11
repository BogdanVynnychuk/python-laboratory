#Обчислення конкретної функції, в залежності від введеного значення х

import re
def float_input(text):
    pattern = "^-?\d+(\.\d+)?$"
    user_input = input(text)
    while not re.match(pattern, user_input):
        user_input = input("Введене значення некоректне , Введіть число:")
    return float(user_input)
x=float_input("введите X ")
if x<=1:
    y=0
    print("F(x)= ", y)
elif x>1:
    y=1/(x+5+1)
    print("F(x)= ", y)
else:
    print("error")