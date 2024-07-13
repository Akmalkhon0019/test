def raqam(n):
    if n == 0:
        return
    print(n,end= " ")
    raqam(n-1)
n = int(input("Sonni kiriting >:) "))
raqam(n)