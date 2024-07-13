ls = [1,2,6,4,3,2,4,6]
print(ls)
for x in ls:
    while ls.count(x) > 1:
        ls.remove(x)
print(ls)