n = int(input("n = "))
ls = []
for i in range(n):
    if i == 0:
        ls.append(0)
    elif i == 1:
        ls.append(1)
    else:
        ls.append(ls[i-1] + ls[i-2])
print(ls)
sum = 0
for i in range(n):
    sum = sum + ls[i]
print(sum)
