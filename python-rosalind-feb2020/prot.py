import os

sampleDataset = False

if sampleDataset:
    inp = """
    """
    inp = inp.replace('\n', '')

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

mrnaAminoDict =  {
	"uaa": "", "uag": "", "uga": "", "uuu": "F", "uuc": "F",
	"cuu": "L", "cuc": "L", "cua": "L", "cug": "L", "uua": "L",
	"uug": "L","auu": "I", "auc": "I", "aua": "I", "aug": "M",
	"gua": "V", "guu": "V", "gug": "V", "guc": "V", "uca": "S",
	"ucu": "S", "ucg": "S", "ucc": "S", "agu": "S", "agc": "S",
	"cca": "P", "ccu": "P", "ccg": "P", "ccc": "P", "aca": "T",
	"acg": "T", "acu": "T", "acc": "T", "gca": "A", "gcu": "A",
	"gcg": "A", "gcc": "A", "uau": "Y", "uac": "Y", "cac": "H",
	"cau": "H", "cag": "Q", "caa": "Q", "gaa": "E", "gag": "E",
	"ugu": "C", "ugc": "C", "ugg": "W", "cgu": "R", "aau": "N",
	"aac": "N", "aag": "K", "aaa": "K", "gac": "D", "gau": "D",
	"cga": "R", "cgc": "R", "cgg": "R", "aga": "R", "agg": "R",
	"ggu": "G", "ggc": "G", "gga": "G", "ggg": "G"
}

#------

codons = [inp[i:i+3] for i in range(0, len(inp), 3)]

aminoSq = ""

for codon in codons:
    if codon in mrnaAminoDict:
        aminoSq += mrnaAminoDict[codon]
    else:
        print("ERROR codon not in dict: ", codon)
        exit()
print(aminoSq)

