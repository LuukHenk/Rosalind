import os
import re
import urllib.request

practice = False
if practice: sampleInput = """P07204_TRBM_HUMAN"""

#------

def loadInputFile():
    DIR = os.path.dirname(os.path.abspath(__file__))

    INP_FILE = input('Input filename (the file must be in the input dir):\n')
    if os.path.isdir('{}/input'.format(DIR)):
        INP_FILE = 'input/{}'.format(INP_FILE)

    print('Loading \"' + INP_FILE + '\" ...')
    with open(INP_FILE, 'r') as myfile:
        inp = myfile.read()

    return(inp)

def getFastaFile(uniprotID, uniprotWebsite = "https://www.uniprot.org/uniprot/"):
    with urllib.request.urlopen('{}{}.fasta'.format(uniprotWebsite, uniprotID)) as f:
        fastaFile = f.read()

    return(fastaFile)

#------

#load and filter input
inp = sampleInput if practice else loadInputFile()
inp = list(filter(None, inp.split('\n')))
print('---------')

#get fasta files and find the motif
for x in inp:
    fastaFile = str(getFastaFile(x))
    fasta = ''.join(fastaFile.split('\\n')[1:-1])


    motif = re.compile("(?=(N[^P][ST][^P]))")
    motifLocations =  [str(location.start()+1) for location in motif.finditer(fasta)]
    if len(motifLocations) > 0 :
        print('{}\n{}'.format(x, ' '.join(motifLocations)))

