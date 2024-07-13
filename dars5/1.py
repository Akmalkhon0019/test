def local_maximum(ls):
    if type(ls) != list:
        return
    for x in range(1,len(ls) - 1):
        if ls[x] > ls[x-1] and ls[x] > ls[x+1]:
            print(ls[x], end = " ")
if __name__ == '__main__':
    ls = [12,90,45,58,42,65,30]
    print(ls)
    local_maximum(ls)