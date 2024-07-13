def func1(numbers):
    result = sorted(numbers, key = lambda x: x[0])
    return result
numbers = [(2, 4, 5),(1, 2, 3),(3, 2, 1),(5, 4, 6),(9, 7, 8)]
def func2(numbers):
    result = sorted(numbers, key = lambda x: x[1])
    return result
numbers = [(2, 4, 5),(1, 2, 3),(3, 2, 1),(5, 4, 6),(9, 7, 8)]

def func3(numbers):
    result = sorted(numbers, key = lambda x: x[2])
    return result

numbers = [(2, 4, 5),(1, 2, 3),(3, 2, 1),(5, 4, 6),(9, 7, 8)]

print(func1(numbers))
print(func2(numbers))
print(func3(numbers))