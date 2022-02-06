#!/usr/bin/env python3

import os
import re

PRACTICE = False

#------

if PRACTICE:
    PRACTICE_INP = """
        >Rosalind_10
        ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
        >Rosalind_12
        ATCGGTCGAA
        >Rosalind_15
        ATCGGTCGAGCGTGT
    """

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

codon_to_aminoacid = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }

#------

#load input
if PRACTICE:
    inp = PRACTICE_INP.replace(' ', '')
    inp = inp.split('\n')
    inp = list(filter(None, inp))
else:
    inp = ''.join(load_input_file().split('\n'))

inp = [re.sub(r"(Rosalind_\d\d\d\d)", "", x) for x in inp.split('>')[1:]]

#remove the substrings from the dna
dna = inp[0]
for sub in inp[1:]:
    sub_position = dna.find(sub)
    dna = dna[0:sub_position] + dna[sub_position+len(sub):]

#generate protein from the remaining dna
protein = ''
for i in range(0, len(dna), 3):
    codon = dna[i:i+3]

    if len(codon) == 3:
        aminoacid = codon_to_aminoacid[codon]

        if aminoacid:
            protein += aminoacid

print(protein)
