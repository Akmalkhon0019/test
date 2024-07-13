def function(satr):
    ls = []
    for x in satr:
        ls.append(x)
    ls.sort()
    res = ""
    for x in ls:
        res = res + x
    return res

if __name__ == '__main__':
    print(function(input("Satrni kiriting: ")))