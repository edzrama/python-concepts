import random
import secrets
import numpy as np

print('Random...')
# random float in [0,1)
a = random.random()
print(a)

# random float in range [1,10]
a = random.uniform(1,10)
print(a)

# random integer in range [1,10]. 10 is included
a = random.randint(1,10)
print(a)

# random integer in range [1, 10). 10 is excluded
a = random.randrange(1,10)
print(a)

# random float from a normal distribution with mu and sigma
# mu: Mean of the distribution.
# sigma: Standard deviation of the distribution.
a = random.normalvariate(0, 1)
print(a)

# choose a random element from a sequence
a = random.choice(list("ABCDEFGHI"))
print(a)

# choose number of unique random elements from a sequence
a = random.sample(list("ABCDEFGHI"), 3)
print(a)

# choose number of random elements from a sequence but value can be repeated
a = random.choices(list("ABCDEFGHI"),k=3)
print(a)

# shuffle list in place
a = list("ABCDEFGHI")
random.shuffle(a)
print(a)


# The seed() method is used to initialize the random number generator.
# If you use the same seed value twice you will get the same random number twice
print('\nSeed.')

random.seed(1)
print(random.random())
print(random.uniform(1, 10))
print(random.choice(list("ABCDEFGHI")))

print('Re-seeding with 2...')
random.seed(2)  # Re-seed

print(random.random())
print(random.uniform(1, 10))
print(random.choice(list("ABCDEFGHI")))

print('Re-seeding with 1...')
random.seed(1)  # Re-seed

print(random.random())
print(random.uniform(1, 10))
print(random.choice(list("ABCDEFGHI")))

print('Re-seeding with 2...')
random.seed(2)  # Re-seed

print(random.random())
print(random.uniform(1, 10))
print(random.choice(list("ABCDEFGHI")))

# Secrets
print('\nSecrets...')
# random integer in range [0, 10) where 10 is excluded.
a = secrets.randbelow(10)
print(a)

# return an integer with k random bits.
a = secrets.randbits(5)
print(a)

# choose a random element from a sequence
a = secrets.choice(list("ABCDEFGHI"))
print(a)

# Numpy Random
print('\nNumpy Random...')
np.random.seed(1)
# rand(d0,d1,…,dn)
# generate nd array with random floats, arrays has size (d0,d1,…,dn)
print(np.random.rand(3))
# reset the seed
np.random.seed(1)
print(np.random.rand(3))

# generate nd array with random integers in range [a,b) with size n
values = np.random.randint(0, 10, (5, 3))
print(values)

# generate nd array with Gaussian values, array has size (d0,d1,…,dn)
# values from standard normal distribution with mean 0.0 and standard deviation 1.0
values = np.random.randn(5)
print(values)

# randomly shuffle a nd array.
# only shuffles the array along the first axis of a multi-dimensional array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.random.shuffle(arr)
print(arr)