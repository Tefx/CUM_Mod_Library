def add(x, y):
    return x+y

def double(x):
    return x*2

def sum0(*args):
    return sum(args)

def fl(a, b, c):
    return sum(a)/float(b)+c

EXPORTS = {
    "m1": add,
    "m2": double,
    "m3": sum0,
    "m4": fl
}