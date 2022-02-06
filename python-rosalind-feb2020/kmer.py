#!/usr/bin/env python3
" Generation of a k-mer composition array "

import os
import re
import sys
from itertools import product

PRACTICE = False

if PRACTICE:
    PRACTICE_INP = """
    >Rosalind_6431
    CTTCGAAAGTTTGGGCCGAGTCTTACAGTCGGTCTTGAAGCAAAGTAACGAACTCCACGG
    CCCTGACTACCGAACCAGTTGTGAGTACTCAACTGGGTGAGAGTGCAGTCCCTATTGAGT
    TTCCGAGACTCACCGGGATTTTCGATCCAGCCTCAGTCCAGTCTTGTGGCCAACTCACCA
    AATGACGTTGGAATATCCCTGTCTAGCTCACGCAGTACTTAGTAAGAGGTCGCTGCAGCG
    GGGCAAGGAGATCGGAAAATGTGCTCTATATGCGACTAAAGCTCCTAACTTACACGTAGA
    CTTGCCCGTGTTAAAAACTCGGCTCACATGCTGTCTGCGGCTGGCTGTATACAGTATCTA
    CCTAATACCCTTCAGTTCGCCGCACAAAAGCTGGGAGTTACCGCGGAAATCACAG
    """

PATH = os.path.abspath(__file__)
INP_DIR = "{}/input".format(os.path.dirname(PATH))

def load_input_file(inp_file=None):
    " Load the input file (if not in practice mode) "

    if inp_file is None and os.path.exists(INP_DIR):
        inp_file = "{}/rosalind_{}.txt".format(
            INP_DIR, os.path.splitext(os.path.basename(PATH))[0]
        )

    try:
        with open(inp_file, 'r') as myfile:
            inp = myfile.read()
        print("Opened '{}' ...\n-------\n".format(inp_file))
    except IOError:
        print("Unable to locate the input file '{}'".format(inp_file))
        sys.exit()

    return inp

def main():
    " Main function for k-mer composition "

    # set variables
    fasta_naming_style = r"(Rosalind_\d\d\d\d)"
    kmer_size = 4

    # Load fasta data
    raw_fasta_data = PRACTICE_INP if PRACTICE else load_input_file()

    # Format the dna string
    raw_fasta_data = re.sub(r"\s", "", raw_fasta_data).split(">")[1:]
    if len(raw_fasta_data) != 1:
        raise IndexError("""
            Input should only contain one FASTA string;
            More or less than one FASTA identifiers detected ('>')
        """)
    dna_string = re.sub(fasta_naming_style, "", raw_fasta_data[0])
    if not all(i in "ACGT" for i in dna_string):
        raise ValueError("DNA strand contains non-DNA characters")

    # Generate k-mer array
    kmer_count = {}
    product_list = list(product("ACGT", repeat=kmer_size))
    for kmer in product_list:
        kmer_count["".join(kmer)] = 0

    # Count k-mers values
    for position in range(0, len(dna_string) - kmer_size + 1):
        kmer = dna_string[position:position + kmer_size]
        kmer_count[kmer] = kmer_count[kmer] + 1

    # Format desired output
    print(re.sub(r",", "", str(kmer_count.values())[13:-2]))

# Run main scrips
if __name__ == "__main__":
    main()
