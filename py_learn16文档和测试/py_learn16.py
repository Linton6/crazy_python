#!/usr/bin/python
lk = [1,23]
s = lk
def f():
    return 1, 2,3
s, = f()
print(s)