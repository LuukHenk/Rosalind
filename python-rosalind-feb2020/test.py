
from itertools import chain


# function to see if item is in a sublist
def findItem(theList, item):
    for ind in theList:
        if item in ind:
            return str(theList.index(ind))


# function to create list of connections
def connections(sorted_adj_list):
    conns = []
    for index in xrange(0, len(adj_list_merge), 2):
        # see if first number in any sublist
        in_index = findItem(conns, adj_list_merge[index])
        # see if second number in any sublist
        in_index_2 = findItem(conns, adj_list_merge[index+1])
        if in_index:
            conns[int(in_index)].append(adj_list_merge[index+1])
        elif in_index_2:
            conns[int(in_index_2)].append(adj_list_merge[index])
        else:
            conns.append([adj_list_merge[index], adj_list_merge[index+1]])
    return conns

if __name__ == "__main__":
    f = open("input/rosalind_tree.txt", 'r')
    adj_list = [map(int, line.rstrip().split()) for line in f.readlines()]
    n = adj_list.pop(0)[0]
    adj_list.sort()
    print(adj_list)
    f.close()

    adj_list_merge = list(chain.from_iterable(adj_list))
    conns = connections(adj_list_merge)
    conns_list = list(chain.from_iterable(conns))

    nodes = range(1, n+1)
    loners = []
    for i in nodes:
        if i not in conns_list:
            loners.append(i)

    lone_nodes = len(loners) - 1
    branches = len(conns)
    num_edges = lone_nodes + branches

    print num_edges


# import re
# import urllib.request
# import sys
# import time


# def get_protein_fasta(uniprot_id: str) -> str:

#     DATA_URL = 'http://www.uniprot.org/uniprot/{}.fasta'.format(uniprot_id)
#     with urllib.request.urlopen(DATA_URL) as f:
#         protein_sequence = f.read()

#     return protein_sequence


# def get_protein_string(fasta):
#     protein_string = ''.join(str(fasta).split('\\n')[1:-1])

#     return protein_string


# def protein_motif(uniprot_id: str) -> str:
#     protein_sequence = get_protein_fasta(uniprot_id)
#     protein_string = get_protein_string(protein_sequence)

#     pattern = '(?=(N[^P][ST][^P]))'
#     prog = re.compile(pattern)


#     if prog.finditer(protein_string):
#         results = ' '.join([ str(loc.start()+1) for loc in prog.finditer(protein_string) ])
#     else:
#         return


#     return uniprot_id, results


# if __name__ == '__main__':
#     # finding individual motif
#     if len(sys.argv) == 2:
#         uniprot_id, motif = protein_motif(sys.argv[1])
#         if motif:
#             print(uniprot_id)
#             print(motif)
#         sys.exit()

#     with open('input/rosalind_mprt.txt', 'r') as f:
#         lst = f.read().strip().split('\n')

#     for i in lst:
#         uniprot_id, motif = protein_motif(i)
#         if motif:
#             print(uniprot_id)
#             print(motif)
#         time.sleep(1)


#fibonacci_cache = {}

#def fibonacci(n):
#    #if the value is in cache
#    if n in fibonacci_cache:
#        return fibonacci_cache[n]

#    #else compute the Nth term
#    if n == 0:
#        return 1
#    elif n == 1:
#        return 1
#    elif n > 1:
#        value = fibonacci(n-1) + fibonacci(n-2)
#    #cache the value
#    fibonacci_cache[n] = value
#    return value

#for n in range(0, 10):
#    print(fibonacci(n))

##----------- offspring predictor

#import itertools

#def determineoffspring(m = ['aa', 'bb'], f = ['aa', 'bb']):
#    totalgenes = len(m)

#    if len(f) != totalgenes:
#        print('please give mates the same amount of genes')
#        exit()
#        pass

#    allelecombis_m = list(itertools.product(*m))
#    allelecombis_f = list(itertools.product(*f))

#    offspring = []
#    for alleles_m in allelecombis_m:
#        for alleles_f in allelecombis_f:

#            offspringgeneset = []
#            for i in range(totalgenes):
#                offspringgeneset.append(''.join([alleles_m[i], alleles_f[i]]))

#            offspring.append(offspringgeneset)

#    return(offspring)

#currentoffspring = []
#totalgenerations = 2
#currentgeneration = 0
#while currentgeneration != totalgenerations:

#    newoffspring = []
#    if currentgeneration > 0 and len(currentoffspring) > 0:
#        for o in currentoffspring:
#            newoffspring.append(determineoffspring())

#    else:
#        newoffspring.append(determineoffspring())

#    currentoffspring = list(itertools.chain.from_iterable(newoffspring))
#    currentgeneration += 1

