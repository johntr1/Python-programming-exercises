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
        d[i] = i * i;
    return d


# Question 4
def question4(x):
    x = x.split(",")
    return x
print(question4(str(input())))


# Question 5
class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = str(input())

    def printString(self):
        print(self.s.upper())

strO

