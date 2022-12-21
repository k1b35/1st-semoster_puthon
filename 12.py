dots = [(1, 1), (2, 3), (5, 3), (1, 3), (-44, 26)]
lengths = [i[0] * i[0] + i[1] * i[1] for i in dots if i[0] > 0 and i[1] > 0]
# print(lengths)
result = max(lengths)
print(result)
