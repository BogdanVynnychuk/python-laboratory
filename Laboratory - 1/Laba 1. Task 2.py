#Увести з клавіатури дійсні числа х і у, не рівні одне одному.
#Менше з цих двох чисел замінити половиною їх суми, а більше - їх подвоєним добутком.
import re
def float_input(text):
    pattern = "^-?\d+(\.\d+)?$"
    user_input = input(text)
    while not re.match(pattern, user_input):
        user_input = input("Введене значення некоректне , Введіть число:")
    return float(user_input)
x= float_input("Введите х")
y= float_input("Введите у")
if x==y:
    print("Значения равны")
elif x<y:
    print("x=",(x+y)/2)
    print("y=",x*y*2)
elif x>y:
    print("x=", x * y * 2)
    print("y=", (x + y) / 2)