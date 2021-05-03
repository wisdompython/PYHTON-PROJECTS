#itertools

#PRODUCT
from itertools import product
a = [1,2]
b = [2,3]
prod = product(a,b, repeat=2)
print(list(prod))

#permutations
from itertools import permutations
c= [1,2,2,3,34,5]
perm = permutations(a, 2)
print(list(perm))

# combinations
from itertools import combinations, combinations_with_replacement
t = [4,5,6,7,8,9,0,13]
comb = combinations(t, 2)
print(list(comb))
comb_wr = combinations_with_replacement(t, 2)
print(list(comb_wr))

from itertools import accumulate
# gives sums of the list, more like the sum of a arithmetic progression
import operator
# can bring in other basic functions
print(t)
acc = accumulate(t, func=max)
print(list(acc))

from itertools import groupby
# def smaller_than_3(x):
#     return x < 3
# group_obj = groupby(t, key=smaller_than_3)
# for k , v  in group_obj:
#     print(k, list(v))

# persons = [{'name ': 'bimbo', 'age': 23}, {'name ': 'pelumi', 'age': 24},
#            {'name ': 'wisdom', 'age': 23}, {'name ': 'isaac', 'age': 43}]
#
# gp_by = groupby(persons, key=lambda x: x['age'])
# for k, v in gp_by:
#     print(k,list(v))

from itertools import count, cycle, repeat
for i in count(10):
    print (i)
    if i == 20:
        break
# for i in cycle(t):
#     print(i)

for i in repeat(t,40):
    print(i)