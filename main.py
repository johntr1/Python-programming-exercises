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
    str