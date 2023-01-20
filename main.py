import math


# Question 1
def question1():
    li = []
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            li.append(str(i))
    return li


# Question 2

def fact(x):
    # Checks if x == 0 then the code ends
    if x == 0:
        return 1
    # This return is looping the code without a while loop
    return x * fact(x - 1)


# x = int(input())
# print(fact(x))

# Question 3
def question3():
    # Define the number n as an input
    n = int(input())
    # Define d as a dictionary
    d = dict()
    # The loop loops over every number between 1 and n
    for i in range(1, n + 1):
        d[i] = i * i
    return d


# Question 4
def question4(x):
    x = x.split(",")
    return x


# print(question4(str(input())))


# Question 5
class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = str(input())

    def printString(self):
        print(self.s.upper())


# Question 6
def question6():
    C = 50
    H = 30
    D = input().split(",")
    D_new = []
    value = []
    for i in range(0, len(D)):
        D_new.append(int(D[i]))
        value.append(round(math.sqrt((2 * C * D_new[i]) / H)))

    return value


# print(question6())

# Question 7
def question7():
    # Definierar listan som en sträng och splittar
    arr = str(input("string")).split(",")
    # Omvanndlar alla separata strängar till en integer i en loop
    dim = [int(x) for x in arr]
    # Skriver en nollmatris med hjälp av en list-loop
    multilist = [[0 for col in range(dim[1])] for row in range(dim[0])]
    for i in range(0, dim[0]):
        for j in range(0, dim[1]):
            multilist[i][j] = i * j
    print(multilist)


# print(question7())

# Question 8
def question8():
    str_input = input("String").split(",")
    str_sorted = sorted(str_input)
    print(','.join(str_sorted))


# print(question8())

# Question 9
def question9():
    lines = []
    while True:
        str_input = str(input("String"))
        if str_input:
            lines.append(str_input.upper())
        else:
            break

    print(' '.join(lines))


# print(question9())

# Question 10
def question10():
    li = []
    while True:
        s = str(input("Str"))
        if s:
            li.append(s)
        else:
            break

    s = set(li)
    l = list(s)
    print(" ".join(l))


# print(question10())

# Question 11
def question11():
    num = input().split(",")
    li = []
    for i in range(0, len(num)):
        if int(num[i], 2) % 5 == 0:
            li.append(num[i])
    print(','.join(li))


# print(question11())

# Question 12
def question12():
    li = []
    for i in range(1000, 3001):
        if i % 2 == 0:
            li.append(str(i))
    print(','.join(li))


# print(question12())


# Question 13
def question13():
    inp = str(input())
    d = {"LETTERS": 0, "DIGITS": 0}
    for i in range(0, len(inp)):
        if inp[i].isdigit():
            d['DIGITS'] += 1
        elif inp[i].isalpha():
            d['LETTERS'] += 1

    print('LETTERS', d['LETTERS'], 'DIGITS', d['DIGITS'])


# print(question13())

# Question 14
def question14():
    inp = str(input())
    d = {"UPPER CASE": 0, "LOWER CASE": 0}
    for i in range(0, len(inp)):
        if inp[i].isupper():
            d['UPPER CASE'] += 1
        elif inp[i].islower():
            d['LOWER CASE'] += 1

    print('UPPER CASE', d['UPPER CASE'], 'LOWER CASE', d['LOWER CASE'])


# print(question14())


# Question 15

def question15():
    inp = str(input())
    value = 0
    for i in range(0, 4):
        value = value + int(inp * (i + 1))

    print(value)

# print(question15())


# Question 16
def question16():
    inp = input().split(',')
    li = []
    for i in range(0, len(inp)):
        if int(inp[i]) % 2 != 0:
            li.append(inp[i])
    print(','.join(li))


print(question16())






