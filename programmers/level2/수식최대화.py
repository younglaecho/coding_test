import copy
def plus(numbers, operator):
    numbers1 = copy.copy(numbers)
    operator1 = copy.copy(operator)
    while True:
        for i in range(len(operator1)):
            if operator1[i] == '+':
                numbers1[i] = numbers1[i] + numbers1[i+1]
                del numbers1[i+1]
                del operator1[i]
                break
        if '+' not in operator1:
            break
    return numbers1, operator1
def minus(numbers, operator):
    numbers1 = copy.copy(numbers)
    operator1 = copy.copy(operator)
    while True:
        for i in range(len(operator1)):
            if operator1[i] == '-':
                numbers1[i] = numbers1[i] - numbers1[i+1]
                del numbers1[i+1]
                del operator1[i]
                break
        if '-' not in operator1:
            break
    return numbers1, operator1

def x(numbers, operator):
    numbers1 = copy.copy(numbers)
    operator1 = copy.copy(operator)
    while True:
        for i in range(len(operator1)):
            if operator1[i] == '*':
                numbers1[i] = numbers1[i] * numbers1[i+1]
                del numbers1[i+1]
                del operator1[i]
                break
        if '*' not in operator1:
            break
    return numbers1, operator1

def pmx(numbers, operator):
    numbers, operator = plus(numbers, operator)
    numbers, operator = minus(numbers, operator)
    numbers, operator = x(numbers, operator)
    return abs(numbers[0])


def pxm(numbers, operator):
    numbers, operator = plus(numbers, operator)
    numbers, operator = x(numbers, operator)
    numbers, operator = minus(numbers, operator)
    return abs(numbers[0])

def mxp(numbers, operator):
    numbers, operator = minus(numbers, operator)
    numbers, operator = x(numbers, operator)
    numbers, operator = plus(numbers, operator)
    return abs(numbers[0])

def mpx(numbers, operator):
    numbers, operator = minus(numbers, operator)
    numbers, operator = plus(numbers, operator)
    numbers, operator = x(numbers, operator)
    return abs(numbers[0])

def xpm(numbers, operator):
    numbers, operator = x(numbers, operator)
    numbers, operator = plus(numbers, operator)
    numbers, operator = minus(numbers, operator)
    return abs(numbers[0])

def xmp(numbers, operator):
    numbers, operator = x(numbers, operator)
    numbers, operator = minus(numbers, operator)
    numbers, operator = plus(numbers, operator)
    return abs(numbers[0])


def solution(expression):
    tmp=''
    numbers = []
    operator = []
    for char in expression:
        if char=='*' or char=='-' or char=='+':
            numbers.append(tmp)
            operator.append(char)
            tmp=''
            continue
        tmp+=char
        
    numbers.append(tmp)
    numbers = list(map(int, numbers))
    return max(pmx(numbers,operator), pxm(numbers, operator), mpx(numbers, operator), mxp(numbers, operator), xpm(numbers, operator), xmp(numbers, operator))

