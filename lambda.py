# lambda
points2d = [(1,4), (3,7), (5,-1), (6,10)]
points2d_sorted = sorted(points2d, key=lambda x: x[0] + x[1])
print(points2d)
print(points2d_sorted)

#map function
a = [1, 2, 4, 5,6]
b = map(lambda x : x*2, a)
print(list(b))
# you can also achieve this with
c = [x*2 for x in a]
print(c)

#filter function
names = ['James', 'Isaac', 'Veronica']
print(names)
print(id(names))
names[2] = 'Sarah'
print(names)
print(id(names))

