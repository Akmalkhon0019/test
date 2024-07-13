dict1 = {1: "ABC", 2: "DEF", 3: "GHI", 4: "JKL", 5: "MNO"}
dict2 = {}
for key, value in dict1.items():
    dict2[key] = value

for key, value in dict2.items():
    dict1[key] = dict2[key]

print(dict1)
