### Introduction to Algorithms Tutorial ###

# ReCodEx: homework solution + new homework

## Ancestor Check ##

# Write a function isAncestor(p, q) that takes pointers to two nodes p and q in a binary tree
# and returns true if p is an ancestor of q.

def is_ancestor(p, q):
    if p is None or q is None:
        return False

    if p.left is q or p.right is q:
        return True

    return is_ancestor(p.left, q) or is_ancestor(p.right, q)

## Complete Tree ##

# Write a function that takes a binary tree and returns True if the tree is complete.

def is_complete(root):
    def check(t):
        if t is None:
            return 0, True

        ld, lc = check(t.left)
        rd, rc = check(t.right)
        return max(ld, rd) + 1, ld == rd and lc and rc

    _, c = check(root)
    return c

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

## Empty Buckets ##

# Suppose that we insert N values into a hash table with N buckets. What fraction of the buckets do we expect
# will be empty? Assume that N is a large number.

# The chance of a value *not* ending up in a given bucket is 1 - 1/N. The chance of N values all not
# ending up in that bucket is (1 - 1/N)^N. You might know that this number approaches 1/e (where
# e is the base of natural logarithm; 2.718281828) as N grows to infinity. We thus expect the number of
# empty buckets to be N/e on average.

import random

def simulate_hashing(N, factor=100):
    buckets = N * [0]
    for _ in range(factor * N):
        buckets[random.randrange(N)] += 1
    return buckets

def empty_buckets(N):
    buckets = simulate_hashing(N, 1)
    return sum(1 for x in buckets if x == 0)

# >>> empty_buckets(1000000)
# 367587
# >>> 1000000 / math.e
# 367879.44117144233

## Random Queue ##

# We'd like to implement a data structure RandomQueue with the following interface:

# q.add(x) – add an element to the queue

# q.remove() - removes a random element from the queue

# q.is_empty() - test if a RandomQueue is empty

# All operations should be fast, i.e. not run in linear time. How can we implement this structure?

# We can use a dynamic array. add adds a new element at the end; is_empty is trivial. remove
# swaps a random element in the dynamic array with the element at the end and then removes it
# (which can be done in O(1)). Everything runs in (potentially amortized) O(1).

### Programming 1 Tutorial ###

# ReCodEx: homework solution + new homework


## Flatten a Matrix ##

# Write a function flatten() that takes a matrix and returns a list containing
# all the values from all rows:

# >>> flatten([[5, 2], [6, 10], [8, 3]])
# [5, 2, 6, 10, 8, 3]

# Use a list comprehension.

def flatten(m):
    return [x for row in m for x in row]

## Deep Flatten ##

# Write a function deep_flatten that takes a list that may contain sublists
# nested to any level. The function should return a list containing all the
# values from all the sublists:

# >>> deep_flatten([ [[5, 2], 6], [8, 3], [[[[10]]]] ])
# [5, 2, 6, 8, 3, 10]

def deep_flatten(nested):
    result = []
    def go(l):
        if isinstance(l, list):
            for x in l:
                go(x)
        else:
            result.append(l)
    go(nested)
    return result

def deep_flatten_nonrecursive(nested):
    i = 0
    while i < len(nested):
        if isinstance(nested[i], list):
            nested[i:i + 1] = nested[i]  # replace the range [i, i+1) with the list nested[i]
        else:
            i += 1
    return nested

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

## First to Pass ##

# a) Write a function first(f, l) that takes a function f and a list l. The function should
# return the index of the first value x in l such that f(x) is true. If there is no such value, return -1.

# b) Using the function you wrote in part (a), write a function first_begin(ss, c) that takes a list of
# strings ss and a character c, and returns the index of the first string in the list that begins with
# the character c, or -1 if there is no such string.

def first(f, l):
    for i, x in enumerate(l):
        if f(x):
            return i
    return -1

def first_begin(ss, c):
    return first(lambda s: len(s) > 0 and s[0] == c, ss)
