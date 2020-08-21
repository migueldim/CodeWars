"""
This time we want to write calculations using functions and get the results. Let's have a look at some examples:
    seven(times(five())) # must return 35
    four(plus(nine())) # must return 13
    eight(minus(three())) # must return 5
    six(divided_by(two())) # must return 3
"""

def zero(f = None): return 0 if not f else f(0)
def one(f = None): return 1 if not f else f(1)
def two(f = None): return 2 if not f else f(2)
def three(f = None): return 3 if not f else f(3)
def four(f = None): return 4 if not f else f(4)
def five(f = None): return 5 if not f else f(5)
def six(f = None): return 6 if not f else f(6)
def seven(f = None): return 7 if not f else f(7)
def eight(f = None): return 8 if not f else f(8)
def nine(f = None): return 9 if not f else f(9)

def plus(y): return lambda x: x+y
def minus(y): return lambda x: x-y
def times(y): return lambda  x: x*y
def divided_by(y): return lambda  x: x/y

#def zero(arg=None):
#    if arg is None:
#        return 0;
#    return operation(arg[0],0,arg[1:])
#def one(arg=None): 
#    if arg is None:
#        return 1
#    return operation(arg[0],1,arg[1:])
#def two(arg=None): 
#    if arg is None:
#        return 2
#    return operation(arg[0],2,arg[1:])
#def three(arg=None):
#    if arg is None:
#        return 3
#    return operation(arg[0],3,arg[1:])
#def four(arg=None): 
#    if arg is None:
#        return 4
#    return operation(arg[0],4,arg[1:])
#def five(arg=None): 
#    if arg is None:
#        return 5
#    return operation(arg[0],5,arg[1:])
#def six(arg=None): 
#    if arg is None:
#        return 6
#    return operation(arg[0],6,arg[1:])
#def seven(arg=None):
#    if arg is None:
#        return 7
#    return operation(arg[0],7,arg[1:])
#def eight(arg=None):
#    if arg is None:
#        return 8
#    return operation(arg[0],8,arg[1:])
#def nine(arg=None):
#    if arg is None:
#        return 9
#    return operation(arg[0],9,arg[1:])


#def operation(op, a, b):
#    if op == '+': 
#        return int(a) + int(b)
#    if op == '-': 
#        return int(a) - int(b)
#    if op == '*': 
#        return int(a) * int(b)
#    if op == '/': 
#        return int(int(a) / int(b))

#def plus(arg): 
#    return "+" + str(arg)
#def minus(arg):
#    return "-" + str(arg)
#def times(arg): 
#    return "*" + str(arg)
#def divided_by(arg): 
#    return "/" + str(arg)


print(seven(times(five()))) # must return 35
print(four(plus(nine())))# must return 13
print(eight(minus(three())))# must return 5
print(six(divided_by(four()))) # must return 3
print(four(plus(two(times(five())))))