numbers = [9, 10, 4, 7, 6, 8, 2]
result = list(map(lambda x: numbers[x] ** 2, range(len(numbers))))
print(result)