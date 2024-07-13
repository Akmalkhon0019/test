mytuple = ()
mylist = list(mytuple)
newlist = list(map(lambda x: x**2, mylist))
sortedtuple = tuple(sorted(newlist))
mytuple = tuple
print(sortedtuple)