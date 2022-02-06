#!/usr/bin/env python3

""" Complementing a Strand of DNA """

### Question ###

# In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
# The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement sc of s.

### Explanation ###

# In this exercise we want to get the reverse complements (look it up if you don't know the term) of a DNA string. This exercise consists of two steps; first we want to reverse the DNA string (AAAAT -> TAAAA) and secondly we want to find the complementary base for each nucleotide (A <-> T and C <-> G). (TAAAA -> ATTTT). In addition to the 'standard script' explained in rna.py, we now also added the possibility to load input files.

### EXERCISE ###

# Standard script #

# Import operating system to access files
import os
import re

PRACTICE = True

if PRACTICE:
    PRACTICE_INP = """
        GATGGAACTTGACTACGTAAATT
    """

# Get the path of the executed file (this file)
PATH = os.path.abspath(__file__)

# Set the /input folder, in the folder of this file as input directory
INP_DIR = "{}/input".format(os.path.dirname(PATH))

# Function to load input file
def load_input_file(INP_FILE = ""):

    # If there is no specific input file given, search for the file input/rosalind_revc.txt (in this case). Search for "python3 file loading" if you want to know how it works.
    if INP_FILE == "" and os.path.exists(INP_DIR):
        INP_FILE = "{}/rosalind_{}.txt".format(INP_DIR, os.path.splitext(os.path.basename(PATH))[0])

    # Try to open and read the input file (read to INP)
    try:
        with open(INP_FILE, 'r') as myfile:
            INP = myfile.read()

        print('Opened \"{}\" ...\n-------\n'.format(INP_FILE))

    # If we are not able to open the file, give an error and close the program
    except IOError:
        print('Unable to locate the input file {}'.format(INP_FILE))
        exit()

    # return the variable containing the text of the file
    return INP

#--------------------

# use practice input if PRACTICE is True, else load the input file in the input/ folder
inp = PRACTICE_INP if PRACTICE else load_input_file()

# Remove all whitespace from the input using Regex
dna = re.sub(r'\s', '', inp)


# Method 1 #

#first reverse the dna string (in Python you use [::-1] to reverse a string)
dna_reverse = dna[::-1]

# Save the bases with it complements in a dictionary (Key: value). If you call the key 'A' you get the value 'T'. (Search "Python3 dictionaries" if you don't know the concept.)
complementary_bases = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

#make the output variable dna_complementary and find the complementary base for each base.
dna_complementary = ''
for base in dna_reverse:
    dna_complementary += complementary_bases[base]

#now we have our complementary dna strand
print(dna_complementary)


# Method 2 #

#you can convert all the lines above in these two lines below to make the program quicker
complementary_bases = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
print(''.join([complementary_bases[base] for base in dna[::-1]]))

