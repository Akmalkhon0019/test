# 1-masala
# def func1(numbers):
#     sortedList = sorted(numbers, key = lambda x: x[2])
#     return sortedList

# def func2(numbers):
#     sortedList = sorted(numbers, key = lambda x: x[1])
#     return sortedList

# def func3(numbers):
#     sortedList = sorted(numbers, key = lambda x: x[0])
#     return sortedList

# if __name__ == "__main__":

#     numbers = [(2, 4, 5), (1, 2, 3), (3, 2, 1), (5, 4, 6), (9, 7, 8)]
#     print(func1(numbers))
#     print(func2(numbers))
#     print(func3(numbers))

# 2-masala

# numbers = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# sortedList = sorted(numbers, key = lambda x:sum(int(digit) for digit in str(x)))

# print(sortedList)

# 3-masala

# mytuple = (10, 4, 3, 5, 6, 7, 4, 1)

# mylist = list(mytuple)

# newlist = list(map(lambda x: x**2, mylist))

# sortedtuple = tuple(sorted(newlist))

# print(sortedtuple)