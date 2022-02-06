import os

practice = False
if practice:
    practiceInput = """
        >Rosalind_1
        ATCCAGCT
        >Rosalind_2
        GGGCAACT
        >Rosalind_3
        ATGGATCT
        >Rosalind_4
        AAGCAACC
        >Rosalind_5
        TTGGAACT
        >Rosalind_6
        ATGCCATT
        >Rosalind_7
        ATGGCACT
        """

#------

def loadInputFile():
    PATH = os.path.abspath(__file__)
    INP_DIR = '{}/input'.format(os.path.dirname(PATH))

    if os.path.exists(INP_DIR):
        INP_FILE = '{}/rosalind_{}.txt'.format(INP_DIR, os.path.splitext(os.path.basename(PATH))[0])

    try:
        with open(INP_FILE, 'r') as myfile:
            INP = myfile.read().split('>')[1:]
        print('Opened \"{}\" ...\n-------\n'.format(INP_FILE))
    except IOError:
        print('Unable to locate the input file {}'.format(INP_FILE))
        exit()

    return(INP)

#------

#load input
if practice:
    inp = practiceInput.replace(' ', '')
    inp = inp.split('>')
else:
    inp = loadInputFile()

#create dataset from input
dataset = {}
for x in inp:
    x = x.split('\n')
    if len(x[1]) > 0:
        dataset[x[0]] = ''.join(x[1:])

#create and fill the matrix
matrix = [{'A': 0, 'C': 0, 'G': 0, 'T': 0} for i in range(0, len(list(dataset.values())[0]))]
for x in dataset:
    for i, y in enumerate(dataset[x]):
        matrix[i][y] += 1

#format output
outString = ''
outMatrix = ['A:', 'C:', 'G:', 'T:']
for x in matrix:
    outString += max(x, key=x.get)
    outMatrix[0] += ' {}'.format(x['A'])
    outMatrix[1] += ' {}'.format(x['C'])
    outMatrix[2] += ' {}'.format(x['G'])
    outMatrix[3] += ' {}'.format(x['T'])

#print output
print(outString)
for x in outMatrix:
    print(x)

