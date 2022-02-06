#!/usr/bin/env python3
""" Run in Python3 enviroment """

import os
import sys
import re

PRACTICE = False

if PRACTICE:
    FASTA_NAME_STYLE = "(Rosalind_\d\d)"

    PRACTICE_INP = """
        >Rosalind_14
        TATGCTAAGATC
        >Rosalind_18
        ACG
    """

if not PRACTICE:
    FASTA_NAME_STYLE = "(Rosalind_\d\d\d\d)"

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
    Main function of the script. Returns one collection of indices that represent the location
    of a given substring in a string
    """

    inp = PRACTICE_INP if PRACTICE else load_input_file()
    inp = re.sub(r"\s", "", inp).split(">")[1:]
    inp = [re.sub(re.compile(FASTA_NAME_STYLE), "", x) for x in inp]

    string = inp[0]
    substring = inp[1]

    # print("{}\n{}\n".format(string, substring))

    out = []
    index = 0
    for nucl in substring:
        # Find first substring location in string
        substring_loc = string[index:].find(nucl)

        # Move the index after the substring location
        index = index + substring_loc + 2

        # Add the index position to the output
        out.append(str(index - 1))

    print(" ".join(out))

#------

if __name__ == "__main__":
    main()
