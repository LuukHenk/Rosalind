#-----Solved with recursion

def populationSizeCalculator(totalMonths = 5, nestSize = 3, adults = 1, offspring = 0, currentMonth = 1):
    print(currentMonth, adults)
    if currentMonth == totalMonths:
        print(adults, ' adults in the ', totalMonths, '\'th month.')

    else:
        newOffspring = adults * nestSize
        adults = offspring + adults
        offspring = newOffspring
        populationSizeCalculator(totalMonths, nestSize, adults , offspring, currentMonth + 1)

M = int(input('How many months?\n'))
S = int(input('What is the nest size?\n'))
A = int(input('How many adults in the first month?\n'))
populationSizeCalculator(M, S)



#------ Solved with while loop

# M = 34   #total months
# S = 4       #size of offspring
# A = 1       #adults in the first month
# O = 0       #offspring in the first month
# C = 1       #current month

# while C < M:
#     N = A * S
#     A = O + A
#     O = N
#     C += 1

# print(A)

