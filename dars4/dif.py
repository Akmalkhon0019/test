set1 = {1,2,3}
set2 = {3,4,5}
farq = set1.difference(set2)

print(farq)
farq = set2.difference(set1)

print(farq)
farq = set1.symmetric_difference(set2)

print(farq)

a = {1,2,3}
b = {3,4,5}
c = a.difference(b)
print(c)
print(a ^ b)
name = {"Lamin": 10, "Noyer": 1, "Kross": 8}
print(name)
kesishma = a.intersection(b)
print(kesishma)
a.remove(3)
print(a)
b.discard(4)
print(b)
a.add(7)
print(a)