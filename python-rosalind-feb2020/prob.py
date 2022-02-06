#!/usr/bin/env python3
""" Run in Python3 enviroment """

import os
import sys
import math

PRACTICE = False

if PRACTICE:
    PRACTICE_INP = """
        ACGATACAA
        0.129 0.287 0.423 0.476 0.641 0.742 0.783
    """

PATH = os.path.abspath(__file__)
INP_DIR = '{}/input'.format(os.path.dirname(PATH))

#------

def load_input_file(inp_file=''):
    """Returns content of inp_file"""

    if inp_file == '' and os.path.exists(INP_DIR):
        inp_file = '{}/rosalind_{}.txt'.format(INP_DIR, os.path.splitext(os.path.basename(PATH))[0])

    try:
        with open(inp_file, 'r') as myfile:
            inp = myfile.read()

        print('Opened \"{}\" ...\n-------\n'.format(inp_file))

    except IOError:
        print('Unable to locate the input file {}'.format(inp_file))
        sys.exit()

    return inp

def main():
    """
    Main function of the script. Prints the common logarithm of the probability that a
    random string constructed with the GC-content found in the input file
    """

    # Load and format input
    inp = PRACTICE_INP if PRACTICE else load_input_file()
    inp = list(filter(None, inp.split("\n")))
    inp = [list(filter(None, x.split(" "))) for x in inp]

    # Get content from input
    strand = inp[0][0]
    gc_contents = list(map(float, inp[1]))

    # Count GC and AT content in the input strand
    gc_in_strand = strand.count("C") + strand.count("G")
    at_in_strand = len(strand) - gc_in_strand

    # Calculate probablity of the construction of the string
    out = []
    for k in gc_contents:
        chance_perfect_gc_match = (k / 2) ** gc_in_strand
        chance_perfect_at_match = ((1 - k) / 2) ** at_in_strand
        log_chance_perfect_match = math.log10(chance_perfect_gc_match * chance_perfect_at_match)
        out.append(str(round(log_chance_perfect_match, 3)))

    # Print the probabilities (in common logarithm)
    print(" ".join(out))

#------

if __name__ == "__main__":
    main()
