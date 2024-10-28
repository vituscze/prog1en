### Introduction to Algorithms Tutorial ###

# ReCodEx: homework solution + new homework

# How to efficiently search for a value in a list? If we don't know anything
# else about the elements of a list, the best we can do is a sequential search:

def find(a, k):
    for i in range(len(a)):
        if a[i] == k:
            return i
    return -1

# What is the time complexity of this search in the best and worst case?
# For best case we have O(1) since the value we're looking for could be
# the first one; for the worst case we have O(n) since it could also be
# the last one or it could not be present in the list at all.

# The reason why we can't do better than O(n) is that comparing an element of
# the list with the searched value doesn't tell us anything other about the
# other elements, so we have no choice but to try them all. What if we knew
# something else about the list? Sometimes, the list will be *sorted*. Is it
# possible to find a value in a sorted list faster than O(n)?

# Suppose the list is sorted in an increasing order. If we look at the element
# in the middle and find out it's *smaller* than what we're looking for, we
# immediately know that the value can't be in the first half of the list (those
# elements are even smaller). We thus only need to consider the second half.

def bsearch(a, k):
    # The variable lo keeps track of the start of the currently considered range
    # (including the element at position lo). At the start of the search, it's set
    # to zero.
    lo = 0
    # Similarly, the variable hi keeps track of the end of the range. At the start
    # of the search, it's set to len(a) - 1 (the last element in the array).
    hi = len(a) - 1
    # Next up, we keep halving the range until we either find what we're looking
    # for or the range becomes empty. Note that when lo == hi, the range isn't
    # empty yet; it contains just a single element.
    while lo <= hi:
        # Find the middle position of the current range
        mid = (lo + hi) // 2
        if a[mid] == k:
            # We were lucky and the middle element is the one we're looking for
            return mid
        if a[mid] < k:
            # Middle point is too small; what we're looking for can't be in the
            # first half
            lo = mid + 1
        else:
            # Middle point is too large; what we're looking for can't be in the
            # second half
            hi = mid - 1
    # The range is empty and no value was found: it couldn't have been in the list
    return -1

# Does this function always finish? In each step, we decrease the length of the
# range by at least one so it has to eventually either find the element or reach
# an empty range.

# What's the best case time complexity? If the value is in the middle, we find
# it immediately -- O(1). In the worst case, the value isn't present in the list
# and we have to shrink the range to just a single element (after which the loop
# ends). Notice that in each iteration of the loop, we remove half of the range.
# How many times do we have to do that until the range has just a single element?
# O(log n).

# Suppose the list contains multiple elements that have the value k. What happens
# to lo and hi if we remove the first if (i.e. the one with a[mid] == k)?
# Is that useful in any way?

## Random Array ##

# Write a program that reads an integer N and generates a random array of N
# integers in ascending order. The first number in the array should be 0, and
# the difference between each pair of consecutive array elements should be
# a random number from 1 to 10.

# Next, the program should generate N new random integers in the range from 0
# to 10 · N. The program should count how many of these integers are present
# in the array, and print this count.

# If the input number N is large, what value do you think this program will
# print, approximately?

import random

def generate(n):
    result = [0]
    value = 0
    for i in range(n - 1):
        value += random.randint(1, 10)
        result.append(value)
    return result

def count(n):
    array = generate(n)
    found = 0
    for _ in range(n):
        if bsearch(array, random.randint(0, 10 * n)) != -1:
            found += 1
    return found

# The generated list contains n numbers from 0 to 10 * n, i.e. about 10% of the
# range. A randomly picked number thus has about 10% chance of being in the list.

## Integer Square Root ##

# Write a program that reads an integer n ≥ 0 and prints the square root of n
# (if it is an integer), or otherwise 'Not a square'. Do not use any
# floating-point numbers. Your program should run in O(log n).

def isqrt(n):
    # Suppose we had an array of squares a = [0, 1, 4, 9, 16, 25, ..., n * n].
    # The defining property of this array is that a[i] == i * i. If we wanted
    # to find the square root of any number, we just need to find the correct
    # index, which we can do with binary search. The question is: can we do this
    # without creating the entire array (which would take too long)?
    lo = 0
    hi = n
    while lo <= hi: # At least one number in the range
        mid = (lo + hi) // 2
        if mid * mid == n: # a[mid] == mid * mid
            return mid
        if mid * mid < n:
            lo = mid + 1
        else:
            hi = mid - 1
    return None

n = int(input())
sqrt_n = isqrt(n)
if sqrt_n is None:
    print('Not a square')
else:
    print(sqrt_n)

### Programming 1 Tutorial ###

# ReCodEx: homework solution + new homework

## Building a List ##

# Consider this program:

# n = int(input('Enter n: '))
# a = []
# for i in range(n):
#     a += [i]

# Will this program run in O(n) or O(n^2)? Perform an experiment to find out.
# (recall that += is the same as extend(...))

def bad(n):
    a = []
    for i in range(n):
        a = a + [i]

def good(n):
    a = []
    for i in range(n):
        a.append(i)

def maybe(n):
    a = []
    for i in range(n):
        a += [i]

import matplotlib.pyplot as plt
import random
import time

def test(f, n):
    start = time.time()
    f(n)
    end = time.time()
    return end - start

def plot():
    xs = range(5000, 40000, 5000)
    good_data = []
    bad_data = []
    maybe_data = []
    for n in xs:
        good_data.append(test(good, n))
        bad_data.append(test(bad, n))
        maybe_data.append(test(maybe, n))

    plt.plot(xs, good_data, label = 'good')
    plt.plot(xs, bad_data, label = 'bad')
    plt.plot(xs, maybe_data, label = 'maybe')
    plt.legend()
    plt.xlabel('n')
    plt.ylabel('time (sec)')
    plt.show()

## Column with Largest Number ##

# Write a program that reads a square matrix of integers. The program should
# print the largest value in the matrix and the column number that contains it.

# Input:
#
# 2 8 3
# 9 6 7
# 0 3 -1
#
# Output:
#
# Column 1 contains 9.

import math
import sys

matrix = []
for line in sys.stdin:
    row = []
    for n in line.split():
        row.append(int(n))
    matrix.append(row)
matrix = [[2,8,3],[9,6,7],[0,3,-1]]
# print(matrix)
size = len(matrix)  # We can assume it's a square matrix
largest = -math.inf
col = None
for i in range(size):
    for j in range(size):
        if matrix[i][j] > largest:
            largest = matrix[i][j]
            col = j + 1
print(f'Column {col} contains {largest}.')

## Identity Matrix ##

# The identity matrix of size N x N contains ones along its main diagonal, and zeroes everywhere else.
# For example, here is the identity matrix of size 4 x 4:
#
# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1
#
# Write a function identity_matrix(n) that returns the identity matrix of size n x n,
# represented as a list of lists.

def id_matrix(n):
    m = [n * [0] for _ in range(n)]
    for i in range(n):
        m[i][i] = 1
    return m

## Matrix Sum ##

# Write a function that takes two matrices, and returns the sum of the matrices.
# Assume that the matrices have the same dimensions.

def add_matrix(a, b):
    # We need to create a new matrix with same dimensions as a and b, but
    # notice we cannot just do a.copy() because the copy is *shallow*.
    c = [len(a[0]) * [0] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[i])):
            c[i][j] = a[i][j] + b[i][j]
    return c

# What's the time complexity?

## Matrix Product ##

# Write a function that takes two matrices, and returns the product of the matrices.
# Assume that the matrices have dimensions that are compatible for multiplication.

def mul_matrix(a, b):
    rows_a = len(a)
    shared = len(b)  # We can assume the sizes are compatible
    cols_b = len(b[0])

    # Final matrix has dimensions rows_a x cols_b
    c = [cols_b * [0] for _ in range(rows_a)]
    for i in range(len(c)):
        for j in range(len(c[i])):
            for k in range(shared):
                c[i][j] += a[i][k] * b[k][j]
    return c

# What's the time complexity?

## Special Pythagorean triplet ##

# Solve Project Euler's problem 9:

# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

# Simplest solution:
for a in range(1, 1001):
    for b in range(1, 1001):
        c = 1000 - a - b
        if a * a + b * b == c * c:
            print(a, b, c, a * b * c)
# Problem: it finds 200 375 425 and then 375 200 425
# We could also check that a <= b, but we can instead make our loops a bit more clever:
for a in range(1, 1001):
    for b in range(a, 1001):  # No reason to check b < a
        c = 1000 - a - b
        if a * a + b * b == c * c:
            print(a, b, c, a * b * c)
# We can save some time by breaking from the inner loop when we find c < b. It's only going to
# get smaller after that point.
for a in range(1, 1001):
    for b in range(a, 1001):  # No reason to check b < a
        c = 1000 - a - b
        if c < b:
            break
        if a * a + b * b == c * c:
            print(a, b, c, a * b * c)

## Largest product in a series ##

# Solve Project Euler's problem 8:

# Find the thirteen adjacent digits in the 1000-digit number that have the
# greatest product. What is the value of this product?

number = '''
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
'''

digits = []
for d in number:
    if '0' <= d <= '9':
        digits.append(int(d))

# We could try all starting positions for the 13 digits and compute the
# product for each. This would definitely work, but wouldn't be feasible for
# larger number of digits. Can we do it better? If the number had no zeros,
# we could keep track of the product of the last 13 digits and when moving one
# digit forward, divide by the last digit and multiply by the new digit.
# To handle zeros, we just need to remember how many of them are in the last 13
# digits!

product = 1
product_len = 0
zeros = 0
highest = 0

for i in range(len(digits)):
    # Add a digit
    product_len += 1
    if digits[i] == 0:
        zeros += 1
    else:
        product *= digits[i]
    # (Possibly) remove a digit
    if product_len > 13:
        product_len -= 1
        if digits[i - 13] == 0:
            zeros -= 1
        else:
            product //= digits[i - 13]
    # If we have 13 digits in our product and none of them are zeros...
    if product_len == 13 and zeros == 0 and product > highest:
        highest = product

print(highest)
