n = int(input("n ni kiriting: "))
numbers = list(map(int, input(f"{n} ta butun sonni kiriting: ").split()))

sonlar = []
for num in numbers:
    if num % 11 == 0:
        sonlar += [num]  
if sonlar:
    eng_katta = max(sonlar)
    print(f"11 ga bo'linuvchi eng katta son: {eng_katta}")
else:
    print("11 ga bo'linuvchi son topilmadi.")

