from functools import reduce
from itertools import accumulate

# lambda arguments: expression
add10 = lambda x: x + 10
print(add10(5))

multiplier = lambda x, y: x * y
print((multiplier(2, 7)))

points_xy = [(1, 2), (15, 3), (11, 2), (-3, 3), (10, 4)]
points_xy_sorted = sorted(points_xy)
print(points_xy)
print(points_xy_sorted)
# sort by second argument
points_xy_sorted = sorted(points_xy, key=lambda val: val[1])
print(points_xy_sorted)
# sort by sum
points_xy_sorted = sorted(points_xy, key=lambda val: val[0] + val[1])
print(points_xy_sorted)

# map() function returns a map object(which is an iterator) of the results
# after applying the given function to each item of a given iterable (list, tuple etc.)
# map(fun, iter)
list_a = [1, 2, 3, 4, 5]
list_b = map(lambda x: x * 2, list_a)
print(list(list_b))
# is same result as list comprehension
list_c = [x * 2 for x in list_a]
print(list_c)

# The filter() function extracts elements from an iterable (list, tuple etc.)
# filter(function, iterable)
list_d = filter(lambda x: x % 2 == 0, list_a)
print(list(list_d))
# is same result as list comprehension
list_e = [x for x in list_a if x % 2 == 0]
print(list_e)

# Reduce Function - returns single value
# reduce(fun,seq)
# first two elements of sequence are picked and the result is obtained.
# Next step is to apply the same function to the previously attained result
# and the number just succeeding the second element and the result is again stored.
# This process continues till no more elements are left in the container.
# The final returned result is returned and printed on console.
product_a = reduce(lambda x, y: x * y, list_a)
print(product_a)

# accumulate - returns a iterator containing the intermediate results.
# accumulate(seq,fun)
sum_a = accumulate(list_a, lambda x, y: x * y)
print(list(sum_a))
