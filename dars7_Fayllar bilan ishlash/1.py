filename = input("Fayl k-ng:>  ")
f = open(filename,"wt")
for x in range(1,10,2):
    f.write(str(x) + " ")
