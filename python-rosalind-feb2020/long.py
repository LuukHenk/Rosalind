#!/usr/bin/env python3

import os
import re
import sys

FASTA_NAME_STYLE = "(Rosalind_\d\d\d\d)"
PRACTICE = True

#------

if PRACTICE:
    PRACTICE_INP = """
        >Rosalind_56
        ATTAGACCTG
        >Rosalind_57
        CCTGCCGGAA
        >Rosalind_58
        AGACCTGCCG
        >Rosalind_59
        GCCGGAATAC
    """

    FASTA_NAME_STYLE = "(Rosalind_\d\d)"

PATH = os.path.abspath(__file__)
INP_DIR = '{}/input'.format(os.path.dirname(PATH))

def load_input_file(INP_FILE = ''):
    if INP_FILE == '' and os.path.exists(INP_DIR):
        INP_FILE = '{}/rosalind_{}.txt'.format(INP_DIR, os.path.splitext(os.path.basename(PATH))[0])

    try:
        with open(INP_FILE, 'r') as myfile:
            INP = myfile.read()

        print('Opened \"{}\" ...\n-------\n'.format(INP_FILE))

    except IOError:
        print('Unable to locate the input file {}'.format(INP_FILE))
        sys.exit()

    return INP

# Try to combine strings in a list to build one long superstring
def superstring(strands):
    min_overlap_len = round(len(strands[0]) / 2)
    new_strands = []

    # Compare all input strands
    for i, x in enumerate(strands):
        for j, y in enumerate(strands):
            if i != j:

                # Determine if the first part of y can also be found in x
                y_min_overlap = y[:min_overlap_len]
                if y_min_overlap in x:
                    index_y_in_x = re.search(y_min_overlap, x).start()

                    # Combine strands if the last part of x also can be found in y
                    if index_y_in_x != 0 and x[index_y_in_x:] in y:
                        new_strands.append(x[:index_y_in_x] + y)

    # Return unique strands
    return list(set(new_strands))

#main function to format a superstring using the practice input or a file
def main(input_file_name=''):

    # Load practice input or load input file if practice is False
    inp = PRACTICE_INP if PRACTICE else load_input_file(input_file_name)

    # Format input to a list with the DNA strands in string format
    inp = re.sub(r"\s", "", inp).split(">")[1:]
    inp = [re.sub(re.compile(FASTA_NAME_STYLE), "", x) for x in inp]

    # Determine if the list has enough strings to combine
    if len(inp) == 0 or not isinstance(inp, list):
        print("Please input a list with at least one string")
        inp = None

    else:
        #Try to combine the strings while there is not one long superstring
        while len(inp) > 1:
            inp = superstring(inp)

    return inp[0]

#------

if __name__ == "__main__":
    print(main())
