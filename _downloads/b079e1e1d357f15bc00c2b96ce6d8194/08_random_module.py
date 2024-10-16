"""
RANDOM MODULE - random module provides a number of functions that can be used to
generate random numbers. Random numbers are used in various applications such as
games, simulations, cryptography, and statistical analysis.

    - True Random Number Generator (TRNG)
        - generates random numbers based on physical processes such as
          atmospheric noise, radioactive decay, or thermal noise.
        - The random numbers generated by a TRNG are truly random.
        - They are completely unpredictable and uniformly distributed.
        - They are slow and expensive to implement.

    - Pseudo-Random Number Generator (PRNG)
        - generates random numbers using a deterministic algorithm.
        - The random numbers generated by a PRNG are not truly random.
        - They are predictable and reproducible.
        - They can be initialized with a seed value, which determines the sequence
          of random numbers generated.
        - They are fast and efficient.

Some of the commonly used functions in the random module are:
1. random() - generates a random float number between 0 and 1.
2. randint() - generates a random integer number between two specified integers.
3. uniform() - generates a random float number within a specified range.
4. seed() - initializes the random number generator.
5. randrange() - generates a random integer number within a specified range with a step.
   syntax: random.randrange(start, stop, step)
6. choice() - returns a random element from a sequence.
7. choices() - returns a random sample of elements from a sequence with replacement.
8. sample() - returns a random sample of elements from a sequence without replacement.
9. shuffle() - shuffles the elements of a sequence.

"""
# import the random module
import random

# generate a random float number between 0 and 1
print(random.random())  # Output: 0.6394267984578837

# generate a random integer number between 1 and 10
print(random.randint(1, 10))  # Output: 7

# generate a random float number between 1 and 10
print(random.uniform(1, 10))  # Output: 5.123456789012345

# initialize the random number generator with a seed value
random.seed(10)

# generate a random integer number between 1 and 10
print(random.randint(1, 10))  # Output: 10

# generate a random integer number between 1 and 10 with a step of 2
print(random.randrange(1, 10, 2))  # Output: 7

# generate a random element from a sequence
print(random.choice([1, 2, 3, 4, 5]))  # Output: 3

# generate a random sample of elements from a sequence with replacement
print(random.choices([1, 2, 3, 4, 5], k=3))  # Output: [3, 1, 5]

# generate a random sample of elements from a sequence without replacement
print(random.sample([1, 2, 3, 4, 5], k=3))  # Output: [3, 1, 5]

# shuffle the elements of a sequence
arr = [1, 2, 3, 4, 5]
random.shuffle(arr)
print(arr)  # Output: [3, 1, 5, 2, 4]
