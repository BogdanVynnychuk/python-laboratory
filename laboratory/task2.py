x= int(input("Введите х"))
y= int(input("Введите у"))
if x==y:
    print("Значения равны")
elif x<y:
    print("x=",(x+y)/2)
    print("y=",x*y*2)
elif x>y:
    print("x=", x * y * 2)
    print("y=", (x + y) / 2)