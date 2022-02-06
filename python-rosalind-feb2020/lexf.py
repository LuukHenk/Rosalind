#!/usr/bin/env python3
""" Enumerating k-mers Lexicographically """

import os
import sys
import itertools

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
    Main function of the script.
    """
    # Load input
    inp = load_input_file()

    # Make dataset of input
    inp = list(filter(None, inp.split("\n")))

    # Use itertools product to find the possible combinations of inp[0] with a length of inp[1]
    out = list(itertools.product(inp[0].split(" "), repeat=int(inp[1])))

    # Output the data to a file
    fil = open("output/lexf.txt", "w")
    for string in out:
        fil.write("".join(string))
        fil.write("\n")
    fil.close()
    print("Written file to 'output/lexf.txt'")

#------

if __name__ == "__main__":
    main()
