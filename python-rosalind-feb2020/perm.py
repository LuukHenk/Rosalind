#!/usr/bin/env python3

import itertools

inp = 0
while inp < 1 or inp > 7:
    inp = int(input('Please gave in integer between 1 and 7:\n'))

inp = range(1, inp+1)

#---------

def easy_method(x):
    return list(itertools.permutations(x))

def advanced_method(lst):
    #basis cases
    if len(lst) == 0:
        yield []
    elif len(lst) == 1:
        yield lst

    #use recursion to build the list
    else:
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i+1:]

            for p in advanced_method(xs):
                yield [x]+p

#---------

perm = easy_method(inp)
perm = tuple(advanced_method(list(inp)))

f = open('output/perm.txt', 'w')
f.write('{}\n'.format(str(len(perm))))
[f.write('{}\n'.format(" ".join(map(str, p)))) for p in perm]
