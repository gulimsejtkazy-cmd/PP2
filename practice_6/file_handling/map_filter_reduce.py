# 1
from functools import reduce

nums = [1, 2, 3, 4, 5]

# map
squared = list(map(lambda x: x**2, nums))

# filter
even = list(filter(lambda x: x % 2 == 0, nums))

# reduce
sum_all = reduce(lambda x, y: x + y, nums)

print(squared)
print(even)
print(sum_all)
# 2
from functools import reduce

nums = [1, 2, 3, 4, 5]

print(list(map(lambda x: x**2, nums)))
print(list(filter(lambda x: x % 2 == 0, nums)))
print(reduce(lambda x, y: x + y, nums))