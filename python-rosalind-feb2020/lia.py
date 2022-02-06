def bernoulliTrails(N, K, Ps):
    import scipy.special
    return(scipy.special.binom(N, K) * (Ps ** K) * ((1 - Ps) ** (N - K)))

#this question is actually an example of Bernoulli Trials
generation = int(input('For which generation do we want to determine the probability?\n'))
print('\n')

successes = int(input(''.join(['How many succeses must there be in the ', str(generation), '\'th generation?\n'])))
print('\n')

#calculate the true N (#total trails instead of the generation (2 offspring per generation))
totalTrails = 2**generation

#chance for AaBb is 25% with 2 AaBb parents
Ps = 0.25

#calculate the chance for not having a success
X = []
for i in range(0, successes):
    X.append(bernoulliTrails(totalTrails, i, Ps))

#1- not having a success == succes :)
print('Chance is: ', round(1 - sum(X), 3))
