#!/usr/bin/env python3
""" Transitions and Transversions """

import os
import sys

PRACTICE = False

if PRACTICE:
    PRACTICE_INP = """
    >Rosalind_0209
    GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
    AGTACGGGCATCAACCCAGTT
    >Rosalind_2200
    TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
    GGTACGAGTGTTCCTTTGGGT
    """
    PRACTICE_INP = PRACTICE_INP.replace(" ", "")
    PRACTICE_INP = PRACTICE_INP.replace("\n", "")

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
    Main function of the script. Determine the transition/transversion ratio of a mutated DNA strand
    """

    # Load input data
    inp = PRACTICE_INP if PRACTICE else load_input_file()

    # Construct dataset from input data
    dna_sets = [dataset[13:] for dataset in inp.split(">")[1:]]

    # Dataset size control
    if len(dna_sets) != 2 or len(dna_sets[0]) != len(dna_sets[1]):
        print("Error: Maximum of two DNA sets. DNA sets must also be of similar length")
        sys.exit()

    # Determine the transition/transversion ratio
    transitions = {"A": "G", "G": "A", "C": "T", "T": "C"}
    count = {"transition": 0, "transversion": 0}
    for i in range(0, len(dna_sets[0])): # For each base in the DNA strand
        if dna_sets[0][i] != dna_sets[1][i]: # Check if the bases aren't similar
            if dna_sets[1][i] == transitions[dna_sets[0][i]]: # Check if the base is a transion
                count["transition"] += 1
            else:
                count["transversion"] += 1
    print(count["transition"]/count["transversion"]) # Print the transition/transversion ratio

#------

if __name__ == "__main__":
    main()
