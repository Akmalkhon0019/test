def isPrime(x):
    j = 2
    while (j ** 2 <= x):
        if (x % j == 0):
            return False
        j += 1
        return True
ls = list(map(int,input("c>> : ").split()))
prime_number = filter(isPrime,ls)
print(type(prime_number))
for x in prime_number:
    print(x, end = " ")
