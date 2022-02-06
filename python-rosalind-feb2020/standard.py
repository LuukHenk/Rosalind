#!/usr/bin/env python3
""" Run in Python3 enviroment """

import os
import sys

PRACTICE = True

if PRACTICE:
    PRACTICE_INP = """
    ADD INP
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
    Main function of the script. ADD GOAL OF FUNCTION
    """

    inp = PRACTICE_INP if PRACTICE else load_input_file()
    print(inp)

#------

if __name__ == "__main__":
    main()
