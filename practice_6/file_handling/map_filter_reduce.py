# 1
from functools import reduce

nums = [1, 2, 3, 4, 5]

# map
squared = list(map(lambda x: x**2, nums))
print("Squares:", squared)
#applies a function to all elements

# filter
even = list(filter(lambda x: x % 2 == 0, nums))
print("Even:", even)
# leaves only elements where the condition is True

# reduce
sum_all = reduce(lambda x, y: x + y, nums)

print(sum_all)
# reduce takes a list and “compresses” it into a single value
# 2
from functools import reduce

nums = [1, 2, 3, 4, 5]

print(list(map(lambda x: x**2, nums)))
print(list(filter(lambda x: x % 2 == 0, nums)))
print(reduce(lambda x, y: x + y, nums))
