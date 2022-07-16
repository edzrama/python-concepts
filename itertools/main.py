from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat
import operator

# product
a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(list(prod))

# permutations
# return all number of possible arrangements
new_list = [1, 2, 3]
perm = permutations(new_list)
print(list(perm))
# with len
perm = permutations(new_list, 2)
print(list(perm))

# combinations
new_list2 = [1, 2, 3]
combo = combinations(new_list2, 2)
print(list(combo))
# combinations_with_replacement
new_list2 = [1, 2, 3]
combo_wr = combinations_with_replacement(new_list2, 2)
print(list(combo_wr))

# accumulate -  add values from left to right
new_list3 = [1, 2, 3, 4, 5]
acc = accumulate(new_list3)
print(list(acc))
#  accumulate but multiply
acc_multiply = accumulate(new_list3, func=operator.mul)
print(list(acc_multiply))


# groupby
list_grp = [1, 2, 3, 4, 5]
group = groupby(list_grp, key=lambda x: x < 3)
for key, val in group:
    print(key, list(val))

people = [{'name': 'Jon', 'age': 20}, {'name': 'James', 'age': 20}, {'name': 'Jane', 'age': 23}, {'name': 'Jeff', 'age': 23}, {'name': 'Janine', 'age': 25}]
print(people)
group2 = groupby(people, key=lambda x: x['age'])
for key, val in group2:
    print(key, list(val))