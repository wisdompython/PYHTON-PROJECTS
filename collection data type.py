# collections : counter, namedtuple, OrderedDict, defaultd ict, deque
# from collections import Counter # stores elements as dictionary keys and counts as values
# boy = "wwweedddsssaaasf"
# my_counter = Counter(boy)
# print(my_counter)
# print(my_counter.most_common(2))
# print(list(my_counter.elements()))


from collections import namedtuple
Point = namedtuple('Point' , ' x , y')
pt = Point(4 , 9)
print(pt.x,pt.y)

from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 6
print(ordered_dict)

from collections import defaultdict
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['a'])

from collections import deque
#double ended queue, you can remove and add to both  ends

D = deque()
D.append(3)
D.append(5)
D.extendleft('1234566')
print(D)
D.rotate(-1)
print(D)