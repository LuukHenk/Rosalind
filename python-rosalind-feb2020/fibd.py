#-----Solved with recursion

def populationSizeCalculator(bornPerMonth, totalMonths=5, adults=0, offspring=1, currentMonth=1):
    if currentMonth == totalMonths:
        print(adults, ' adults and ', offspring, ' offspring in the ', totalMonths,
              '\'th month. (', adults + offspring, ' in total)')

    else:
        newOffspring = adults
        adults = offspring + adults - bornPerMonth[0]
        bornPerMonth.append(newOffspring)
        bornPerMonth = bornPerMonth[1:]
        offspring = newOffspring
        populationSizeCalculator(bornPerMonth, totalMonths, adults, offspring, currentMonth + 1)

M = int(input('How many months?\n'))
L = int(input('What is the lifespawn?\n'))
bornPerMonth = [0 for i in range(L-1)] + [1]

populationSizeCalculator(bornPerMonth, M)



#------ Solved with while loop

# M = 6   #total months
# L = 3   #lifespan
# A = 0   #adults
# O = 1   #offspring
# B = [0 for i in range(L-1)] + [1] #rabbits that were born each month
# C = 1   #current month

# while C < M:
#     N = A
#     A += O - B[0]
#     B.append(N)
#     B = B[1:]
#     O = N
#     C += 1

# print(A + O)
