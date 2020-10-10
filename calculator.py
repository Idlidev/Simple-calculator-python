num1 = input("Number 1 equals :- ")
num2 = input("Number 2 equals :- ")

operation = input("operation :- ")


def add():
    sum = float(num1) + float(num2)
    print("The sum is equal to :- ")
    print(sum)


def subtract():
    difference = float(num1) - float(num2)
    print("The difference is equal to :- ")
    print(difference)


def multiply():
    product = float(num1) * float(num2)
    print("The product is equal to :- ")
    print(product)


def divide():
    quotient = float(num1) / float(num2)
    print("The quotient is equal to :- ")
    print(quotient)


if operation == "add":
    add()
elif operation == "subtract":
    subtract()
elif operation == "multiply":
    multiply()
elif operation == "divide":
    divide()
else:
    print("Operations include :- add, subtract, multiply, divide")
