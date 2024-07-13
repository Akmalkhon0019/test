numbers = []
while True:
    num = int(input("Son kiriting: "))
    if num == 0:
        break
    numbers += [num] 
    sch = 0
res = 0
for num in numbers:
    if num % 7 != 0 and num % 5 != 0:
        sch += 1
    if num < 0:
        res += num
print(f"7 ga va 5 ga karra bo'lmagan sonlar soni: {sch}")
print(f"manfiy sonlar yig'indisi: {res}")