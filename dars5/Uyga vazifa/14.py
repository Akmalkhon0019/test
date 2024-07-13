def toq(i,n):
    if i >= n:
        return
    print(i,end = " ")
    return toq(i+2,n)
n = int(input("Sonni kiriting: "))
toq(1,n)