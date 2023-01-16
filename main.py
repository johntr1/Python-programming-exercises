# Question 1
def question1():
    li = []
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            li.append(str(i))
    return li

# Question 2

def fact(x):
    #Checks if x == 0 then the code ends
    if x == 0:
        return 1
    #This return is looping the code without a while loop
    return x * fact(x - 1)
#x = int(input())
#print(fact(x))

# Question 3

