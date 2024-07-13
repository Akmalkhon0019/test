ls = []
n = int(input("List elementlari>>> "))
while n:
	ls.append(int(input(" >>> :")))
	n -= 1
print(ls)
Max,Min = ls[0],ls[0]
for x in ls:
	if (Max < x):
		Max = x
	elif (Min > x):
		Min = x
print("Max = {}".format(Max))
print("Min = {}".format(Min))
