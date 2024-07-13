# import sys
# print(f"Before limit: ",sys.getrecursionlimit())
# sys.setrecursionlimit(1000000)
# print(f"After limit: ",sys.getrecursionlimit())

# def print_number(n = 2000):
#     if n == 0:
#         return
#     print(n,end= " ")
#     print_number(n-1)

# print_number()

#kiritilgan songacha juf sonlarni chiqarish
def even_number(i,n):
    if i > n:
        return
    print(i,end = " ")
    return even_number(i+2,n)
n = int(input("Sonni kiriting: "))
even_number(2,n)
