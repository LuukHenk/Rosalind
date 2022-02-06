#!/usr/bin/env python3

""" Transcribing DNA into RNA """

### Question ###

# An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
# Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.
# Given: A DNA string t having length at most 1000 nt.
# Return: The transcribed RNA string of t.

### Explanation ###

# In this exersize, we want to convert DNA to RNA. In this case we only have to replace all T with U in the input DNA strand. In Python3, we can use the inbuild function 'replace()' to do this.
# For this exersize, we will use more of the 'standard script' than in dna.py. Using the standard script you have the opportunity to choose for practice input or give input yourself.

### EXERCISE ###

# Standard script #

# Import Regex to easily modify input strings
import re

PRACTICE = True

# If practice is true, use practice input as input string
if PRACTICE:
    PRACTICE_INP = """
        GATGGAACTTGACTACGTAAATT
    """

# use practice input if PRACTICE is True, else give input by yourself
inp = PRACTICE_INP if PRACTICE else input("Please paste DNA string:\n")

# Remove all whitespace from the input using Regex
dna = re.sub(r"\s", "", inp)


# Method 1 #

#replace the 'T' with the 'U' in the inp string (input DNA) and print it in the terminal
print(dna.replace("T", "U"))
