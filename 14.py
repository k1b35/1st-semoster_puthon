numbers = ['22', '44', '6', '8', '9']
result = list(map(int, "1 2 3".split()))
resultl = [str(int(x) * int(x)) for x in numbers if int(x) * int(x) % 2 == 0]
print(resultl)