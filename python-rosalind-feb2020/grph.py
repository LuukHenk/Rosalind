import os

sampleDataset = False
codeName = 'Rosalind_0000'
overlap = 3

if sampleDataset:
    inp = """
        >Rosalind_0498
        AAATAAA
        >Rosalind_2391
        AAATTTT
        >Rosalind_2323
        TTTTCCC
        >Rosalind_0442
        AAATCCC
        >Rosalind_5013
        GGGTGGG
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

    print('Loading \"' + INP_FILE + '\" ...')
    inp = ''
    with open(INP_FILE, 'r') as myfile:
        inp = myfile.read().replace('\n', '')

#------

inp = inp.split('>')
inp = inp[1:]

codeLen = len(codeName)
dataset = {}
for x in inp:
    dataset[x[:codeLen]] = [x[codeLen:codeLen+overlap], x[-overlap:]]

output = []
for a in dataset:
    for b in dataset:
        if a == b:
            pass
        elif dataset[a][1] == dataset[b][0]:
            output.append(' '.join([a, b]))

print('\n'.join(output))
