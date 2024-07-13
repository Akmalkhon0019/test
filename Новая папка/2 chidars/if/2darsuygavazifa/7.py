numbers = list(map(float, input("Haqiqiy sonlarni probel bilan ajratib kiriting: ").split()))
kichik_son = None
for num in numbers:
    if num > 20:
        if kichik_son is None or num < kichik_son:
           kichik_son = num
if kichik_son is not None:
    print(f"20 dan katta sonlar orasidagi eng kichik son: {kichik_son}")
else:
    print("20 dan katta son yo'q.")
