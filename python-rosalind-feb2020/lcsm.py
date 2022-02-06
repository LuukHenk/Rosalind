#!/usr/bin/env python3

import os
import re
from datetime import datetime
startTime = datetime.now()

PRACTICE = False

#------

if PRACTICE:
    PRACTICE_INP = """
        >Rosalind_1
        GATTACA
        >Rosalind_2
        TAGACCA
        >Rosalind_3
        ATACA
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

#------

inp = PRACTICE_INP if PRACTICE else load_input_file()
inp = re.sub(r'\s', '', inp)
if PRACTICE:
    inp = [re.sub(r"(Rosalind_\d)", "", x) for x in inp.split('>')[1:]]
else:
    inp = [re.sub(r"(Rosalind_\d\d\d\d)", "", x) for x in inp.split('>')[1:]]

sub_len = len(min(inp, key=len))
x = inp[0]
x_len = len(x)
y_len = len(inp[1:])
matches = False
result = ''

print('Current substring length (without match):')
while sub_len > 0 and not matches:
    offset = 0

    print('{0}\r'.format(sub_len))
    while offset + sub_len <= x_len and not matches:
        match = 0
        for y in inp[1:]:
            if x[offset:sub_len+offset] in y:
                match += 1

        if match == y_len:
            result = x[offset:sub_len+offset]
            matches = True

        offset += 1

    sub_len -= 1

print('Longest common substring:\n{}'.format(result))
print(datetime.now() - startTime)

