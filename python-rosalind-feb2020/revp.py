#!/usr/bin/env python3

import os
import re

fasta_file_name = "(Rosalind_\d\d\d\d)"
PRACTICE = False

#------

if PRACTICE:
    PRACTICE_INP = """
        >Rosalind_24
        TCAATGCATGCGGGTCTATATGCAT
    """

    fasta_file_name = "(Rosalind_\d\d)"

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
        exit()

    return INP

translation = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
def reverse_complements(dna):
    return ''.join([translation[x] for x in dna[::-1]])

#------

#load and format input
inp = PRACTICE_INP if PRACTICE else load_input_file()
inp = re.sub(r'\s', '', inp).split('>')[1:]
inp = [re.sub(re.compile(fasta_file_name), "", x) for x in inp][0]

#determine lenght of the dna of interest
inp_len = len(inp)
for i in range(2, 7):

    #determine start position of the palindrome
    offset = 0
    while (i*2+offset) <= inp_len:

        #determine if dna of interest forms a reverse palindrome
        if inp[offset:i+offset] == reverse_complements(inp[i+offset:i*2+offset]):
            print(offset+1, i*2)
        offset += 1
