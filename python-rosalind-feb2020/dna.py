#!/usr/bin/env python3

""" Counting DNA Nucleotides """

### Question ###

# A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.
# An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."
# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

### Explanation ###

# the principle of the exercise itself is quite simple. You get a text file with  (text) format which is called 'DNA' in our case. And, as the the question thells us, the goal is to count every A, C, G, and T in this string. To count specific characters in a given string we will use an Python inbuild function, called count ( e.g. DNA.count('A') returns the amount of A's in the string DNA). When we count all the nucleotides, we have our answer.

### EXERCISE ###

# Store a DNA string in the 'DNA' variable
DNA = "AAAAA"

# Store the amount of A's in the string DNA in the variable 'a_in_dna'. (5 in this case)
a_in_dna = DNA.count("A")

# We can print this in the terminal (execute the program by typing 'python3 dna.py' in the terminal)
print("Amount of A's in the string DNA: {}".format(a_in_dna))


# Method 1 #

# Now replace the DNA string with the sample dataset from Rosalind to test the sample exersize
DNA = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

# Use print to print the amount of nucleotides counted in the terminal
print("{} {} {} {}\n".format(DNA.count("A"), DNA.count("C"), DNA.count("G"), DNA.count("T")))


# Method 2 #

# We overwrite DNA with given input DNA
DNA = input("Please paste the DNA string from the Rosalind exercise:\n")

# We can also use a dictonary to count the nucleotides using 'key: value'.
nucleotide_counter = {"A": 0, "C": 0, "G": 0, "T": 0}

# Per character in DNA, add value to the key (which is an A, C, G, or T in our case)
for nucleotide in DNA:
    nucleotide_counter[nucleotide] += 1

# Print all values of the nucleotide counter
print(nucleotide_counter["A"], nucleotide_counter["C"],
      nucleotide_counter["G"], nucleotide_counter["T"])


