ls = [
    [1, 'Jean Castro', 'V'], 
    [2, 'Lula Powell', 'V'], 
    [3, 'Brian Howell', 'VI'], 
    [4, 'Lynne Foster', 'VI'], 
    [5, 'Zachary Simon', 'VII']
]
dic = {}
for i in ls:
    dic[i[0]] = [i[1], i[2]]

print(dic)
