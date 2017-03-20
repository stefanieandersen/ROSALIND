# http://rosalind.info/problems/perm/

import math, itertools

f1 = open('answer.txt', 'w+')

integer = 7

number_of_permutations = math.factorial(integer)
integer_range = range(1,integer+1)

combinations = list(itertools.permutations(integer_range))

f1.write(str(number_of_permutations))
f1.write('\n')

for i in combinations:
    f1.write(' '.join(map(str, i)))
    f1.write('\n')
