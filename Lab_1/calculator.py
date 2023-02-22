import constatnts


def my_function(num1, num2, op):
    if op == constatnts.ADD:
        return num1 + num2
    if op == constatnts.SUB:
        return num1 - num2
    if op == constatnts.MULT:
        return num1 * num2
    if op == constatnts.DIV:
        return num1 / num2

    raise Exception("Invalid operation")