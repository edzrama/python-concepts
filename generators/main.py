import sys


def my_generator():
    yield 3
    yield 2
    yield 1


gen = my_generator()
print(gen)

# for _ in gen:
#     print(_)

# print(sum(gen))
# print(sorted(gen))

# will print 1
value = next(gen)
print(value)
# will print 2
value = next(gen)
print(value)
# will print 3
value = next(gen)
print(value)


# will produce 'StopIteration' error because no more yield statement found
# value = next(gen)
# print(value)


def count_down(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1


cd = count_down(4)
print(next(cd))
print(next(cd))
print(next(cd))


# normal function vs generator comparison
# without a generator, the complete sequence has to be stored here in a list
def firstn(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums


print('Normal function')
print(sum(firstn(1000000)))
print(sys.getsizeof(firstn(1000000)), "bytes")


# with a generator, no additional sequence is needed to store the numbers
def first_n_gen(n):
    num = 0
    while num < n:
        yield num
        num += 1


print('\nGenerator function')
print(sum(first_n_gen(1000000)))
print(sys.getsizeof(first_n_gen(1000000)), "bytes")


# Fibonacci sequence
def fibonacci(limit):
    a, b = 0, 1  # first two fibonacci numbers
    while a < limit:
        yield a
        a, b = b, a + b


fib = fibonacci(30)
# generator objects can be converted to a list (only used for printing here)
print(list(fib))


# generator expression vs comprehension
my_new_generator = (i for i in range(100000) if i % 2 == 0)
# print(list(my_new_generator))
print(sys.getsizeof(my_new_generator))
my_dict = [i for i in range(100000) if i % 2 == 0]
# print(my_dict)
print(sys.getsizeof(my_dict))