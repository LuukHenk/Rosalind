import os

sampleDataset = False

if sampleDataset:
    inp = """
    GATATATGCATATACTT
    ATAT
    """
    inp = inp.replace('\n', '>')
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
        inp = myfile.read().replace('\n', '>')

#------

inp = list(filter(None, inp.split('>')))
string = inp[0]
substring = inp[1]
stringLen = len(string)
substringLen = len(substring)

motifPositions = []
currentLocation = 0
while currentLocation <= (stringLen - substringLen):
    if string[currentLocation : currentLocation+substringLen] == substring:
        motifPositions.append(str(currentLocation + 1))
    currentLocation += 1

print(' '.join(motifPositions))
