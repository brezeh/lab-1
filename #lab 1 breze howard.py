#lab 1 breze howard

#define the function/operation selection 
def main():
    operationselect = int(input("enter 1, 2, 3, 4 to choose an operation: "))
    num1 = int(input("enter your first number: "))
    num2 = int(input("enter your second number: "))

    if operationselect == 1:
        print(num1, "+", num2, "=", add(num1, num2))

    elif operationselect == 2:
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif operationselect == 3:
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif operationselect == 4:
        print(num1, "/", num2, "=", divide(num1, num2))

    else:
        print("please enter valid numbers")

#getting results 
#adding numbers 
def add(num1, num2):
    return num1 + num2

#subtracting numbers
def subtract(num1, num2):
    return num1 - num2

#multiplying numbers
def multiply(num1, num2):
    return num1 * num2

#dividing numbers
def divide(num1, num2):
    return num1 / num2

print("please select your operation. 1. add 2. subtract 3. multiply  4. divide")

#call the function
main()