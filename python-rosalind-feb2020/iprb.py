K = int(input('How many homozygous dominant individuals?\n'))
M = int(input('How many heterozygous individuals?\n'))
N = int(input('How many homozygous recessive individuals?\n'))

#------ slow but clear method
# population = []
# for i in range(K): population.append(0)
# for i in range(M): population.append(1)
# for i in range(N): population.append(2)

# dominantChanceSum = 0
# totalPairs = 0

# for i, x in enumerate(population):
#     for y in population[i+1:]:
#         if x == 0 or y == 0:    dominantChanceSum += 1
#         elif x == 1 and y == 1: dominantChanceSum += 0.75
#         elif x == 1 and y == 2: dominantChanceSum += 0.5
#         totalPairs += 1

# print(dominantChanceSum/totalPairs)

#------- fast method

population = [K, M, N]

populationSize = sum(population)


factor = {'0-0': 1,
          '0-1': 1,
          '0-2': 1,
          '1-0': 1,
          '1-1': 0.75,
          '1-2': 0.5,
          '2-0': 1,
          '2-1': 0.5,
          '2-2': 0}


chances = []

for i, x in enumerate(population):
    populationCopy = population[:]

    chanceX = x / populationSize
    populationCopy[i] = populationCopy[i] - 1
    newPopulationSize = populationSize - 1

    for j, y in enumerate(populationCopy):
        chanceY = y / newPopulationSize
        individualTypes = '-'.join([str(i), str(j)])
        chances.append(chanceX * chanceY * factor[individualTypes])

print(sum(chances))
