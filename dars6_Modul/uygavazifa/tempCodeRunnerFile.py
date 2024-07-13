def tortburchak_chop_et(N):
    for i in range(N):
        if i == 0 or i == N - 1:
            print(str(N) * 6)
        else:
            print(str(N) + '    ' + str(N))
N = int(input("Bitta butun sonni kiriting (1 ≤ N < 10): "))
tortburchak_chop_et(N)