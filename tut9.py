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

## Hash Chain Lengths ##

# Write a program that reads an integer N and simulates inserting (100 · N) values into a hash table with
# N buckets using separate chaining, assuming that hash values will be distributed randomly. The program
# should print the lengths of the longest and shortest chains. (You do not need to use an actual hash table
# implementation in solving this exercise.)

import random

def simulate_hashing(N, factor=100):
    buckets = N * [0]
    for _ in range(factor * N):
        buckets[random.randrange(N)] += 1
    return buckets

def min_max_buckets(N):
    buckets = simulate_hashing(N)
    return (min(buckets), max(buckets))

## Empty Buckets ##

# Suppose that we insert N values into a hash table with N buckets. What fraction of the buckets do we expect
# will be empty? Assume that N is a large number.

# The chance of a value *not* ending up in a given bucket is 1 - 1/N. The chance of N values all not
# ending up in that bucket is (1 - 1/N)^N. You might know that this number approaches 1/e (where
# e is the base of natural logarithm; 2.718281828) as N grows to infinity. We thus expect the number of
# empty buckets to be N/e on average.

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

## Heap Check ##

# Write a function that takes an array and returns True if the array represents a valid binary
# heap, otherwise False.

def is_min_heap(array):
    def go(i):
        if i >= len(array):
            return True

        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(array) and array[i] > array[left]:
            return False
        if right < len(array) and array[i] > array[right]:
            return False
        return go(left) and go(right)

    return go(0)

## Heap Positions ##

# Consider a binary min-heap that holds 12 values, with no duplicates.

# How many different array positions are possible for the second smallest value in the heap?

# How many different array positions are possible for the third smallest value in the heap?

# How many different array positions are possible for the fourth smallest value in the heap?

# How many different array positions are possible for the largest value in the heap?

# 2nd smallest value can be anywhere at depth 1; 3rd smallest anywhere at depths 1-2;
# 4th anywhere at depths 1-3; largest value can only be in leaves.

### Programming 1 Tutorial ###

# ReCodEx: new homework

# Section on how to write documentation.

## Index of Largest ##

# Write a function index_largest(a) that takes a list a and returns the index of the largest
# element in a. Use the built-in function max() with a key function.

def index_largest(a):
    return max(enumerate(a), key=lambda x: x[1])[0]

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

## Bijective Function ##

# Write a function bijective(f, n) that takes a function f whose domain and range are the integers 0 .. n – 1.
# The function should return True if f is bijective, i.e. f is both injective (i.e. f(x) ≠ f(y) whenever x ≠ y)
# and surjective (for every y in the range 0 ≤ y < n, there is some x such that f(x) = y).

def bijective(f, n):
    return set(map(f, range(n))) == set(range(n))

## Monotonic Search ##

# Write a function search(f, y, lo, hi, epsilon) takes a function f of a single variable, plus values y, lo, hi
# and epsilon. The function f is guaranteed to be monotonic, i.e. f(x1) < f(x2) whenever x1 < x2. The function
# should find some value x in the range lo ≤ x ≤ hi such that |f(x) – y| <= epsilon. The function should return x,
# or None if there is no such value within the given range lo .. hi. Hint: Use a binary search.

def search(f, y, lo, hi, epsilon):
    if y < f(lo) - epsilon:
        return
    if y > f(hi) + epsilon:
        return

    while True:
        mid = (lo + hi) / 2
        f_mid = f(mid)
        if abs(f_mid - y) <= epsilon:
            return mid
        if y < f_mid:
            hi = mid
        else:
            lo = mid

## Bubble Sort with Key ##

# In the lecture we saw this bubble sort implementation with a key function f:

# Sort the list a, where we consider x to be greater than y
# if f(x) > f(y).
def sort_by(a, f):
    n = len(a)
    for i in range(n - 1, 0, -1):  # n - 1, ... 1
        for j in range(i):
            if f(a[j]) > f(a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]

# This function will call f up to O(N^2) times, where N is the length of a. Rewrite the
# function so that it calls f only N times. Hint: First generate a list of pairs; each
# pair will contain an element x from a, plus the value f(x).
