def add(num1,num2):
    return num1+num2


def subtract(num1,num2):
    return num1-num2


def divide(num1,num2):
    if(num2==0):
        print("not define")
    else:
        return num1/num2


def multiply(num1,num2):
    return num1*num2

a=int(input("a"))
b=int(input("b"))
op=int(input('1/2/3/4'))
if(op==1):
    print(add(a,b))
if(op==2):
    print(subtract(a,b))
if(op==3):
    print(divide(a,b))
if(op==4):
    print(multiply(a,b))