satr = input("So'z kiriting c>: ")
d = {}
for x in satr:
    d[x] = satr.count(x)
for x in d:
    print(f"'{x}' - {d[x]} marta")
