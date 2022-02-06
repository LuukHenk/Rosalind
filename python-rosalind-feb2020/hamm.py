import os

practice = False
if practice:
    sampleInput = """
        GAGCCTACTAACGGGAT
        CATCGTAATGACGGCCT
        """

#------

def loadInputFile():
    DIR = os.path.dirname(os.path.abspath(__file__))

    INP_FILE = input('Input filename (the file must be in the input dir):\n')
    if os.path.isdir('{}/input'.format(DIR)):
        INP_FILE = 'input/{}'.format(INP_FILE)

    print('Loading \"' + INP_FILE + '\" ...')
    with open(INP_FILE, 'r') as myfile:
        INP = myfile.read()

    return(INP)

#------

inp = sampleInput.replace(' ', '') if practice else loadInputFile()
inp = list(filter(None, inp.split('\n')))
print('-----')

hammingDistance = 0
for i in range(0, len(inp[0])):
    if inp[0][i] != inp[1][i]:
        hammingDistance += 1

print(hammingDistance)
