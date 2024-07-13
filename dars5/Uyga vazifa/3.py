a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
juft = list(filter(lambda x: x % 2 == 0,a))
toq = list(filter(lambda x: x % 2 == 1,a))
print("juft >>>: ",juft)
print("toq >>>: ",toq )