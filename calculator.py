import math


def welcome():
    print("Welcome my friend")


flag = True


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


# def math.pow(x, y):
#   return x ^ y


def sin(x):
    return math.sin(math.radians(x))


def cos(x):
    return math.cos(math.radians(x))


def log(x, base):
    return math.log(x, base)


while flag:
    print("please choice selection: ")
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")
    print("5.power")
    print("6.sin")
    print("7.log")
    print("8.cos")

    choice_num = input("Enter your selection:")
    num1 = int(input("please enter num1:"))
    num2 = int(input("please enter num2:"))

try:
    if choice_num == '1':
        print(str(num1) + " +" + str(num2) + " = " + str(add(num1, num2)))
    elif choice_num == '2':
        print(str(num1) + " -" + str(num2) + " = " + str(subtract(num1, num2)))
    elif choice_num == '3':
        print(str(num1) + " *" + str(num2) + " = " + str(multiply(num1, num2)))
    elif choice_num == '4':
        print(str(num1) + " /" + str(num2) + " = " + str(divide(num1, num2)))
    elif choice_num == '5':
        print(str(num1) + " ^" + str(num2) + " = " + str(math.pow(num1, num2)))
    elif choice_num == '6':
        print(math.sin(math.radians(num1)))
    elif choice_num == '7':
        print("log (" + str(num1) + " ," + str(num2) + ") = " + str(math.log(num1, num2)))
    elif choice_num == '8':
        print(math.cos(math.radians(num1)))
    else:
        print("un correct")

except ZeroDivisionError:
    print("division by zero!")

welcome()