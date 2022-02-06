#!/usr/bin/env python3

"""
Enumerating Oriented Gene Orderings
"""

import itertools

def main():
    """
    print the products (2 repeats) of a given input
    """

    #recieve input
    inp = 0
    while inp < 1 or inp > 6:
        inp = int(input('Please gave in integer between 1 and 7:\n'))
    print("-------")

    # Generate a list with all the possible int's for the permutations
    lst = [i for i in range(-inp, inp + 1) if i != 0]

    # Find the permutations
    perms_of_interest = []
    for perm in list(itertools.permutations(lst, inp)):
        # Only remain the unique absolutes of the permutations (so no double values)
        if len(set(map(abs, perm))) == inp:
            perms_of_interest.append(perm)

    # Render the data
    print(len(perms_of_interest))
    for perm in perms_of_interest:
        print(" ".join(map(str, perm)))

if __name__ == "__main__":
    main()
