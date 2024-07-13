# def mushuk():
#     print(" \\   /\\")
#     print(" )  ( ')")
#     print("(  /  )")
#     print(" \\(__)|")

# mushuk()

# print(" \\   /\\")
# print(" )  ( ')")
# print("(  /  )")
# print(" \\(__)|")

# def t(N):
#     for i in range(N):
#         if i == 0 or i == N - 1:
#             print(str(N) * 6)
#         else:
#             print(str(N) + '    ' + str(N))
# N = int(input("Bitta butun sonni kiriting (1 ≤ N < 10): "))
# t(N)

# def tortburchak_qoplama(qatorlar, ustunlar, belgilar):
#     for i in range(qatorlar):
#         if i == 0 or i == qatorlar - 1:
#             qator = belgilar * ustunlar
#         else:
#             qator = belgilar + ' ' * (ustunlar - 2) + belgilar
#         print(qator)
# son = int(input("Bitta butun sonni kiriting: "))
# qatorlar_soni = 4
# ustunlar_soni = 6

# tortburchak_qoplama(qatorlar_soni, ustunlar_soni, str(son))

n = int(input("N kiriting: "))
a = " "
print(n,n,n,n,n,n)
print(n,a,a,a,a,n)
print(n,a,a,a,a,n)
print(n,n,n,n,n,n)