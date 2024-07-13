def juft(i, n):
    if i <= 0:
        return
    print(i, end=" ")
    juft(i - 2, n)

n = int(input("Sonni kiriting <:) "))
juft(n if n % 2 == 0 else n - 1, 0)

