def raqam(n):
    if n < 0:
        return
    raqam(n-1)
    print(n,end= " ")
n = int(input("Sonni kiriting >:) "))
raqam(n)