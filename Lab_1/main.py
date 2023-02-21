def my_function(num1, num2, op):
    if op == "add":
        return num1 + num2
    elif op == "sub":
        return num1 - num2
    elif op == "mult":
        return num1 * num2
    elif op == "div":
        return num1 / num2
    else:
        return "incorrect operation"


print("Hello world")

number1 = int(input("input num 1 : "))
number2 = int(input("input num 2 : "))
operation = input("input operation : ")

print(my_function(number1, number2, operation))
