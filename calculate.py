from get_voice import *
import re


def calculate_the_data(user_input) -> str:
    user_input = user_input.replace(',', '.')
    user_input = low_num_errors(user_input)
    given = user_input.split()
    operation = ''
    prev = ''
    prev_prev = prev
    numbers = []
    for word in given:
        if word in operation_switcher and isDigit(prev):
            operation = word
        elif isDigit(word):
            if prev == 'minus' and not isDigit(prev_prev):
                numbers.append(-float(word))
            else:
                numbers.append(float(word))
        prev_prev = prev
        prev = word
    try:
        return operation_switcher.get(operation)(numbers[0], numbers[1])
    except (IndexError, TypeError):
        return 'Sorry! invalid data'


def low_num_errors(user_input):
    nums = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
    }
    for num in nums:
        user_input = user_input.replace(num, nums.get(num))
    return user_input


def add(op1, op2):
    result = op1 + op2
    op1, op2, result = check_float(op1, op2, result)
    return result


def sub(op1, op2):
    result = op1 - op2
    op1, op2, result = check_float(op1, op2, result)
    return result


def multiply(op1, op2):
    result = op1 * op2
    op1, op2, result = check_float(op1, op2, result)
    return result


def divide(op1, op2):
    try:
        result = op1 / op2
        op1, op2, result = check_float(op1, op2, result)
        return result
    except ZeroDivisionError:
        return "Given data is invalid"


operation_switcher = {
    # ADDITION
    'add': add,
    'added': add,
    'plus': add,
    '+': add,

    # SUBTRACTION
    'subtract': sub,
    'takeoff': sub,
    'subtracted': sub,
    'minus': sub,
    '-': sub,

    # MULTIPLICATION
    'multiply': multiply,
    'multiplied': multiply,
    'times': multiply,
    'x': multiply,
    'X': multiply,

    # DIVISION
    'to divide': divide,
    'divide': divide,
    'divided': divide,

}


def isDigit(word):
    if re.search('^[+-]?[0-9]+$|^[+-]?[0-9]+[.]?[0-9]+$', word):
        return True


def check_float(op1, op2, result):
    if op1.is_integer():
        op1 = int(op1)
    if op2.is_integer():
        op2 = int(op2)
    if result.is_integer():
        result = int(result)
    else:
        result = round(result, 2)
    return op1, op2, result
