import os
from itertools import chain

practice = False
if practice:
    practice_input = """
        >Rosalind_99
        AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG
        """

PATH = os.path.abspath(__file__)
INP_DIR = '{}/input'.format(os.path.dirname(PATH))

#------

def load_input_file():

    if os.path.exists(INP_DIR):
        INP_FILE = '{}/rosalind_{}.txt'.format(INP_DIR, os.path.splitext(os.path.basename(PATH))[0])

    try:
        with open(INP_FILE, 'r') as myfile:
            INP = myfile.read()

        print('Opened \"{}\" ...\n-------\n'.format(INP_FILE))

    except IOError:
        print('Unable to locate the input file {}'.format(INP_FILE))
        exit()

    return(INP)


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

translation = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

def reverse_complements(dna):
    return ''.join([translation[x] for x in dna[::-1]])

def find_orfs(dna, offset = 0):
    #generate protein string
    protein = ''
    for i in range(offset, len(dna), 3):
        codon = dna[i:i+3]

        if len(codon) == 3:
            protein += codon_to_aminoacid[codon]

    #find the open reading frames in the protein string
    orf_start = protein.find('M')
    orf_stop = protein.find('_', orf_start)

    orfs = []
    while orf_start > -1 and orf_stop > orf_start:
        orfs.append(protein[orf_start:orf_stop])
        orf_start = protein.find('M', orf_start+1)
        if orf_start >= orf_stop:
            orf_stop = protein.find('_', orf_start)

    return orfs

#---------

#load input
if practice:
    inp = practice_input.replace(' ', '')
    inp = list(filter(None, inp.split('\n')))[1]
else:
    inp = ''.join(load_input_file().split('\n')[1:])

#get reverse complements of the input
inp_reverse = reverse_complements(inp)

#find the open reading frames (orfs) for all reading frames of the dna input (3 normal and 3 reverse complements)
out = []
for i in range(0, 3):
    out += find_orfs(inp, i)
    out += find_orfs(inp_reverse, i)

#print all unique proteins
print('\n'.join(set(out)))
