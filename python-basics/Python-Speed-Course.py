"""# Remmember && = and; || = or; not = !

# List = array MUTABLE; Tuple = array INMUTABLE
x = [10,9,8,7,6,5,4,3]
x.extend([2,1])
print(len(x))

y = (1,2,3)
# y[0]= 'lol'
print(y[0])

# For loops (start, stop, step)
for i in range(0,30,3):
    print(i)

# enumerate returns index and value
for j, elem in enumerate(x):
    print(j, elem)"""


"""x = [10,9,8,7,6,5,4,3]
# Slice
# start, stop, step (if no values are inputed it will default to either the first, last, 1)
sliced = x[0:4]
split = x[::-1]
print(sliced)
print(split)

# SETS collection that tracks if something exists in the
# s = set()
s = {2, 2, 2, 4, 7, 32}
s.add(2)
print(s)
# -> 7, 4, 32, 1 (random order no duplicates)"""


"""# Dictionaries think of json, key value

dic = {'name': 'Mauricio', 'name2': 'Jose'}
del dic['name2']
print(dic.items())
print(dic['name'])
print('name' in dic)"""

"""# Comprehensions = in line expresions WORKS FOR ALL COLLECTIONS
# value, var, times;
x = [['Mossi' for i in range(5)]for j in range(20)]
print(x)"""

"""# functions
def sayHi(groupsOf, times):
    print([['Hi' for i in range(groupsOf)]for i in range(times)])

sayHi(3, 5)

def sayHello(times):
    counter = times
    print('Hello')
    repeat = counter - 1
    if repeat > 0:
        sayHello(repeat)
    else: print('Loop ended')

sayHello(18)
    
# None marks a optional param
def fun(x, y, z=None):
    print('Run', x, y, z)
    return x*y, x/y

r1, r2 = fun(2, 1, 'z')
print(r1, int(r2))


# functions are objects in py
def returningFunc(x):
    def printFun():
        print(x)
    
    return printFun

returningFunc(4)()

# *var is the equivalent to the spread opperator
def spread(name):
    print([*name])

spread('Mauricio Benjamin Mossi')
"""
def props(*args, **kwargs):
    print(args, kwargs)

props('white', 'black', 'red', 'blue', 'yellow', name='Mauricio')
# ('white', 'black', 'red', 'blue', 'yellow') {'name': 'Mauricio'}





