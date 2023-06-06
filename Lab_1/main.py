from calculator import my_function

print("Hello world")

try:
    number1 = int(input("input num 1 : "))
    number2 = int(input("input num 2 : "))
    operation = input("input operation : ")

    print(my_function(number1, number2, operation))
except Exception as e:
    print(e.args)

numList = list(map(int, input().split()))
evenList = [i for i in numList if i % 2 == 0]
print(evenList)
