numbers = []
while True:
    num = float(input("Son kiriting: "))
    if num == 0:
        break
    numbers = numbers + [num]
count = 0
res = 0
for num in numbers:
    if num % 7 == 0:
        count += 1
        res += num
if count > 0:
    average = res / count
    print(f"7 ga bo'linuvchi sonlar o'rta arifmetigi: {average}")
else:
    print("7 ga bo'linuvchi son mavjud emas.")
