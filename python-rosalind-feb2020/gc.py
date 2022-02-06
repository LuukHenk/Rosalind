import os

sampleDataset = False

#size of the rosalind code (e.g. Rosalind_6404 == 13)
nameSize = 13

if sampleDataset:
    inp = """
        >Rosalind_6404
        CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
        TCCCACTAATAATTCTGAGG
        >Rosalind_5959
        CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
        ATATCCATTTGTCAGCAGACACGC
        >Rosalind_0808
        CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
        TGGGAACCTGCGGGCAGTAGGTGGAAT
    """
    inp = inp.replace('\n', '')
    inp = inp.replace('\t', '')
    inp = inp.replace(' ', '')

else:
    PATH = os.path.abspath(__file__)
    DIR = os.path.dirname(PATH)
    BASENAME = os.path.basename(PATH)

    INP_DIR = 'input'
    INP_FILE = input('Input filename (the file must be in the input dir):\n')
    INP_FILE = '/'.join([INP_DIR, INP_FILE])
    OUT_DIR = '/'.join([DIR, 'output'])
    OUT_FILE = '/'.join([OUT_DIR, os.path.splitext(BASENAME)[0]]) + '.txt'

    print('Opening \"' + INP_FILE + '\" ...')
    inp = ''
    with open(INP_FILE, 'r') as myfile:
        inp = myfile.read().replace('\n', '')

#------

inp = inp.split('>')
inp = inp[1:]

dataset = {}
for s in inp:
    dataset[s[:nameSize]] = s[nameSize:]

gcSet = {}
for r in dataset:
    gcSet[r] = (dataset[r].count('G') + dataset[r].count('C')) / len(dataset[r]) * 100

output = max(gcSet, key=gcSet.get)
print(output, '\n', round(gcSet[output], 6))
