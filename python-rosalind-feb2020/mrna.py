#!/usr/bin/env python3
""" Run in Python3 enviroment """

import os
import sys
import re

PRACTICE = False

if PRACTICE:
    PRACTICE_INP = """
    MA
    """

if not PRACTICE:
    PATH = os.path.abspath(__file__)
    INP_DIR = "{}/input".format(os.path.dirname(PATH))

#------

def load_input_file(inp_file=""):
    """Returns content of inp_file"""

    if inp_file == "" and os.path.exists(INP_DIR):
        inp_file = "{}/rosalind_{}.txt".format(INP_DIR, os.path.splitext(os.path.basename(PATH))[0])

    try:
        with open(inp_file, "r") as myfile:
            inp = myfile.read()

        print("Opened '{}' ...\n-------\n".format(inp_file))

    except IOError:
        print("Unable to locate the input file {}".format(inp_file))
        sys.exit()

    return inp

def main():
    """
    Main function of the script, prints the total number of different RNA strings from
    which the protein could have been translated, modulo 1,000,000
    """

    # Load input file
    inp = PRACTICE_INP if PRACTICE else load_input_file()

    # Remove all whitespace from the input file
    inp = re.sub(r"\s", "", inp)

    # Add stop codon to amino acids
    aminoacids = inp + "_"

    # Possible RNA combinations per amino acid
    possiblilties_for_aminoacid = {
        "A": 4, "C": 2, "D": 2, "E": 2, "F": 2, "G": 4, "H": 2, "I": 3, "K": 2, "L": 6, "M": 1,
        "N": 2, "P": 4, "Q": 2, "R": 6, "S": 6, "T": 4, "V": 4, "W": 1, "Y": 2, "_": 3
        }

    # Count possibilities
    possible_rna_strings = 1
    for aminoacid in aminoacids:
        possible_rna_strings *= possiblilties_for_aminoacid[aminoacid]

    # Print the possibilities modulo 1M
    print(possible_rna_strings % 1000000)

#------

if __name__ == "__main__":
    main()
