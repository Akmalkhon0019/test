#lambda - nomsiz funksiya

ls = [13,15,17,65,13,12,98,8]

natija = filter(lambda x: x % 2 == 1, ls)
#natija = filter(lambda x: x % 2 == 1, ls)
for x in natija:
    print(x, end = " , ")

