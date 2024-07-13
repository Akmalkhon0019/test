numbers = []
while True:
    num = int(input("Son kiriting: "))
    if num == 0:
        break
    numbers += [num]
sch = 0
for num in numbers:
    if num < 0 and num % 2 == 0:
        sch += 1
print(f"Ketma-ketlikda {sch} ta juft manfiy son bor.")

