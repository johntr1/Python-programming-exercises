# li = ['John', 'Jeff', 'Carl']
# d = {}
# for idx, key in enumerate(li):
# d[key] = idx ** 2
# print(d)

# Key decides the value its looping in key (enumerate extract value from list)
# d = {key: idx ** 2 for idx, key in enumerate(li)}
# print(d)

# a = 0b101001
# b = 0b011100
# & Operator returns bit where both have 1 in the same position
# print(f'a = {a:d} = 0b{a :06b}')
# print(a)


# Multiple function expansion:
def multi_return_function(x):
    return x, x ** 2, x ** 3


a, b, c = multi_return_function(13)
print(f'a = {a}, b = {b}, c = {c}')
# Different method:
print('a =', a, 'b =', b, 'c =', c, sep=' ')


def my_function(a, b=2, c=3):
    return a + b + c


print(f'The answer to the function is: {my_function(13)}')

x = [2, 3, 4]


# s = my_sum(x[0], x[1], x[2])
def mySum(a, b, c):
    return a + b + c


# Use *x to use all elements in the list. (Need to have same amount of arguments in list)
print(mySum(*x))

# Lambda functions
axpy_lambda = lambda a, x, y : a*x + y
print(axpy_lambda(2, 3, 4))

# Functions are objects:
def add
