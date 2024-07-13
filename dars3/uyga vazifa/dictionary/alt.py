a = {1,2,3,4,5,6,7,8,9,10}
b = {11,22,33,44,55,66,77,88,99}
c = a.union(b)
c.remove(22)
print(c)
c.discard(44)
print(c)
print(sorted(c))
c.add(119)
print(c)
print(c - a)