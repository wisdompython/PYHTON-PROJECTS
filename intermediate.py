#check the size between a tuple and list
import sys
my_list = ['paul', 'busayo','claro','abbey', 'layo']
my_tuple = ('paul', 'busayo','claro','abbey', 'layo')
print(sys.getsizeof(my_list), 'bytes')
print(sys.getsizeof(my_tuple), 'bytes')
#check the time to create a tuple using the timeit module
import timeit
print(timeit.timeit(stmt="['paul', 'busayo','claro','abbey', 'layo']"))
print(timeit.timeit(stmt="('paul', 'busayo','claro','abbey', 'layo')"))

#dictionaries
my_dict = dict(name= 'paul',age= '24')
print(my_dict)
#popitem method removes the last item
my_dict.popitem()
print(my_dict)
# print(my_dict.popitem())#turns it to a tuple  and removes a random part

# the update method
my_dict = dict(name= 'paul',age= '24')
my_dict2 = dict(city = 'lagos', course = 'crs')
my_dict.update(my_dict2)
print(my_dict)
'''you can use a tuple as key for a dictionary, you cant use a list though because it is mutable unlike tuples '''
my_dict3 = {my_tuple: 5}
print(my_dict3)



#SETS: UNORDERED, MUTABLE, NO DUPLICATES
myset = {1,2,3}
print(myset)
# use dicard,reove,pop,clear methods to remove values from a set
Odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

u = Odds.union(evens)
print(u)

i = Odds.intersection(primes)
print(i)

setA = {1, 2, 3, 4,18}
setB = {1, 2,  4, 5, 6, 7}

diff = setA.difference(setB) # It will remove what is common to both sets and return the rest of SetA.
print(diff)

Diff = setA.symmetric_difference(setB)
print(Diff)

# setA.intersection_update(setB) # this is a like method so it affects the next line of code, and will change the result
# print(setA)

print(setA.issubset(setB))
print(setB.issuperset(setA))
print(setA.isdisjoint(setB))# check if the sets contain the same elements

a = frozenset([1,2,3,4])
print(a)


#STRINGS
from timeit import default_timer as timer
my_list = ['a'] * 1000000

#this is a bad way of writing code
my_string = ""
start = timer()
for i in my_list:
    my_string += i
print(my_string)
stop = timer()
print(stop - start)

#better way to do it
start = timer()
my_string = "".join(my_list)
print(my_string)
stop = timer()
print(stop-start)
 #using the %, format and f-string to edit code
 # if its a digit use %d, or %f for float
 #you can also indicate the no of decimal places say %.2f
var = "wisdom"
my_word = "my name is %s" % var
print(my_word)

# format method
#you can also indicate the no of decimal places say {:.2f}
var2 =  "tobi"
var3 = 3.1234567890
my_Word2 = "my name is {}".format(var2)
my_num = "its {:.2f} pm".format(var3)
print(my_num)
print(my_Word2)

#using the f-string
var4 = "paul"
my_word4 = f"my name is {var4} and {var2}, i like {var3 *4} potatoes"
print(my_word4)