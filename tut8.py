### Introduction to Algorithms Tutorial ###

# ReCodEx: new homework

## Geometric Sum ##

# In the dynamic array class that we saw in the lecture, we started with 10 elements,
# and doubled the number of array elements on every resize operation. We then showed
# that we can grow the array to size N in time O(N), because

# 10 + 20 + 40 + 80 + ... + N = O(N)

# Prove that, more generally, for any starting size S and growth factor R, we have

# S + SR + SR^2 + SR^3 + ... + N = O(N)

# where N = SR^k, the array size after k resize operations.

# If we have f(n) and g(n) and we want to show that f(n) = O(g(n)), we take
# lim n → ∞ f(n)/g(n) and show that it's some finite number.
#
# In our case, the first function is S + SR + ... + SR^k, the second is just SR^k, where S and R
# are constant and our only variable is k. The sequence S + SR + SR^2 + ... + SR^k is called
# a geometric sequence (the ratio of two following terms is constant). You might know that a sum
# of geometric sequence can be computed as:

#     R^(k + 1) - 1
#   S -------------
#         R - 1

# Let's see what happens when we divide this term by SR^k:

#     R^(k + 1) - 1
#   S -------------
#         R - 1        R^(k + 1) - 1   R^k (R - 1/R^k)   R - 1/R^k
#   ---------------- = ------------- = --------------- = ---------
#          SR^k         R^k (R - 1)      R^k (R - 1)       R - 1

# As k gets larger, 1/R^k goes to zero and the whole fraction goes to R/(R - 1), which is some constant.

## Factor of 1.5 ##

# Suppose that in our dynamic array implementation instead of doubling the array size at each step
# we only multiply it by 1.5, which will save memory. By the previous exercise, the time per add()
# operation will still be O(1) on average. However, it will be more expensive by a constant factor,
# which is the price we'll pay for the decreased memory usage.

# Specifically, if we double the array size at each step, then the total cost of all the resize
# operations to grow the array to size N will be proportional to

# f(N) = 1 + 2 + 4 + 8 + ... + N

# If we multiply it by 1.5 at each step, the total cost will be proportional to

# g(N) = 1 + (1.5) + (1.5)^2 + (1.5)^3 + ... = N

# So the increase in cost will be lim N → ∞ [g(N) / f(N)], which is a constant.
# Compute the value of this constant.

# Because we calculated the constant factor exactly, we can just put R into the formula and see
# what happens:

# R = 2 => R/(R - 1) = 2

# So, for a growth factor of 2, we use 2 operations per element (a constant factor of 2).

# R = 1.5 => R/(R - 1) = 3

# As expected, decreasing the growth factor increased the number of operations per element to 3.
# We thus use 1.5 times more operations per element, which is the constant we were looking for.
#
# We can double check by taking a large number that's close to both a power of 2 and a power of 1.5,
# for example 1.26e117 (2^389 or 1.5^665):

# >>> 2.0**389
# 1.2608641982846233e+117
# >>> 1.5**665
# 1.2609192413911928e+117

# Now let's sum 2.0**0 all the way to 2.0**389 (and same for 1.5):
# >>> a = sum(2.0**x for x in range(389+1))
# >>> b = sum(1.5**x for x in range(665+1))
# >>> b / a
# 1.500065482595165

## Modular Hashing ##

# Consider the hash function we saw in the lecture:

B = 0

# Generate a hash code in the range 0 .. 2^32 - 1.
def my_hash(s):
    h = 0
    for c in s:
        d = ord(c)
        h = (B * h + d) % (2 ** 32)
    return h

# a) If B = 0, what hash function will result? Will this be a good hash function?

# b) If B = 1, what hash function will result? Will this be a good hash function?

# c) Suppose that we want to place all unique words of War and Peace into 10,000
# hash buckets. If we use the hash function above, some values of B will be better
# than others, because they will result in a more even distribution of hash values.
# Design an experiment to compare the performance of these choices: B = 2; B = 256;
# B = 257; B = 65,537; B = 1,000,003.

# for B = 0, we have:

# >>> my_hash('a') == my_hash('aha') == my_hash('banana')
# True

# That is, the hash is only using the last letter. For lower-case words,
# this means that the hash would only ever fill a maximum of 26 buckets.
# B = 1 is a bit better, but still not great:

# >>> my_hash('abc') == my_hash('cba') == my_hash('bbb')
# True

# Similarly to the previous hash function, it will have trouble filling up
# the buckets. Even for words of length <= 10, it can only fill 1280 buckets
# (assuming ASCII) and there are MANY more words of length <= 10.

with open('words.txt') as f:
    words = list(f.read().split())

def fill_buckets(newB):
    global B
    B = newB
    buckets = 10000 * [0]
    for w in words:
        buckets[my_hash(w) % 10000] += 1
    return buckets

def buckets_zero(newB):
    return len([x for x in fill_buckets(newB) if x == 0])

def buckets_max(newB):
    return max(x for x in fill_buckets(newB))

def buckets_variance(newB):
    b = fill_buckets(newB)
    avg = sum(b) / len(b)
    return sum(x**2 for x in b) / len(b) - avg**2

# >>> list(map(buckets_zero, [2, 256, 257, 65537, 1000003]))
# [3578, 6277, 1723, 1847, 1772]
# >>> list(map(buckets_max, [2, 256, 257, 65537, 1000003]))
# [20, 365, 9, 10, 9]
# >>> list(map(buckets_variance, [2, 256, 257, 65537, 1000003]))
# [4.96447311, 76.08567311, 1.7798731099999996, 1.9238731099999997, 1.8256731099999994]

# import matplotlib.pyplot as plt
# plt.bar(range(10000), fill_buckets(256))
# plt.show()

### Programming 1 Tutorial ###

# ReCodEx: new homework

# Upcoming deadline for project proposals!

## Flatten a Matrix ##

# Write a function flatten() that takes a matrix and returns a list containing
# all the values from all rows:

# >>> flatten([[5, 2], [6, 10], [8, 3]])
# [5, 2, 6, 10, 8, 3]

# Use a list comprehension.

def flatten(m):
    return [x for row in m for x in row]

## Sum of All Numbers ##

# Write a program that reads any number of lines from standard input, and prints out the sum
# of all numbers on all lines. For example, if the input is

# 2 6 4
# 3 3 2

# then the program will print 20. Write the program in a single line using a list comprehension.

import sys
# print(sum(int(i) for line in sys.stdin for i in line.split()))
print(sum(int(i) for i in sys.stdin.read().split()))

## Largest Matrix Value ##

# Write a function largest_val that takes a matrix and returns the largest value in the matrix,
# along with its coordinates:

# >>> largest_val([[1, 2, 3], [4, 5, 10], [6, 7, 8]])
# (10, (1, 2))

# Write the program in a single line using a list comprehension.

def largest_val(m):
    # return max((m[i][j], (i, j)) for i in range(len(m)) for j in range(len(m[i])))
    return max((x, (i, j)) for i, row in enumerate(m) for j, x in enumerate(row))

## Index Sum ##

# Write a function that takes lists a and b of the same length, and returns the largest
# value of i + a[i] + b[i] for any possible index i. Use the enumerate() and zip() functions
# in your solution.

def index_sum(a, b):
    return max(i + a_i + b_i for i, (a_i, b_i) in enumerate(zip(a,b)))

## Time Class ##

# Write a class Time that represents a time of day with 1-second resolution, e.g. 11:32:07.

# Include an initializer that takes three integers (hours, minutes, seconds) and returns a Time. Seconds should default to 0 if not provided.

# The '+' operator should add a number of seconds to a Time, yielding a new Time object (wrapping past midnight if necessary).

# The '-' operator should subtract two Time objects, yielding a (possibly negative) number of seconds.

# A Time object's string representation should look like this: "11:32:07".

SECONDS_IN_DAY = 24 * 3600

class Time:
    def __init__(self, h, m, s=0):
        self.time = h * 3600 + m * 60 + s
        self.time %= SECONDS_IN_DAY

    # time + number
    def __add__(self, other):
        return Time(0, 0, self.time + other)

    # number + time
    def __radd__(self, other):
        return Time(0, 0, self.time + other)

    def __sub__(self, other):
        return self.time - other.time

    def __repr__(self):
        t = self.time
        s = t % 60
        t //= 60
        m = t % 60
        t //= 60
        h = t
        return f'{h:02d}:{m:02d}:{s:02d}'

## Polynomial Class ##

# Write a class Polynomial representing a polynomial of a single variable. The class should support these operations:

# Polynomial(c) – make a Polynomial with the given coefficients. For example, Polynomial(3, 2, 1) represents the polnomial 3x2 + 2x + 1.

# p.degree() - return the degree of this Polynomial

# The '+' operator should add two Polynomials.

# The '*' operator should multiply two Polynomials.

# p.eval(x) – return the value of the Polynomial at the given value of x

# A Polynomial should have a string representation such as "3x^2 + 2x + 1".
