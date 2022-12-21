nums_first = [1, 2, 3, 5, 8]
nums_second = [2, 4, 8, 16, 32]
result = list(map(lambda x: (nums_first[x] + nums_second[x], nums_first[x] - nums_second[x]), range(len(nums_first))))
# , nums_first[x] - nums_second[x]
print(result)