### Introduction to Algorithms Tutorial ###

# ReCodEx: new homework

## Integer Square Root ##

# Write a program that reads an integer n ≥ 0 and prints the square root of n
# (if it is an integer), or otherwise 'Not a square'. Do not use any floating-point
# numbers. Your program should run in O(log n). (Hint: You can solve this problem
# using a variation of binary search.)

def isqrt(n):
    if n < 0:
        return None
    # There's no need to create an actual list of numbers when
    # we know that the number corresponding to the index ix is
    # simply ix.
    lo = 0
    hi = n
    # We are searching for index such that its square is n.
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo - 1  # return None

n = int(input())
r = isqrt(n)
if r * r == n:
    print(r)
else:
    print('Not a square')

## Missing Number ##

# Write a function that takes an array a with N – 1 elements. The array will contain
# all the integers from 1 .. N in order, except that one integer from that range will
# be missing. Your function should return the value of the missing integer. It should
# run in time O(log N) in the worst case.

# Let's take for example the array [1,2,3,5,6,7]. If we match it with the
# corresponding indices, we get:
#
#  1 2 3 5 6 7
#  0 1 2 3 4 5
#
# We can see that first couple of numbers differ from their index by 1, the
# rest by 2. If we find the position where this change occurs, we have our
# missing number.
def missing(arr):
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == mid + 1:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo + 1

## Adaptive Bubblesort ##

# Modify our implementation of bubblesort from the lecture so that it will exit immediately
# if no elements are exchanged on any pass, since in that case there is no more work to be done.

# With this improvement, what is the best-case and worst-case running time?

def bubble_sort(a):
    n = len(a)
    for i in range(n - 1, 0, -1):   # n - 1 .. 1
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

def better_bubble_sort(a):
    n = len(a)
    for i in range(n - 1, 0, -1):
        swapped = False
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break

import matplotlib.pyplot as plt
import random
import time

def test(f, a):
    start = time.time()
    f(a.copy())
    end = time.time()
    return end - start

def plot():
    xs = range(500, 4000, 500)
    bub = []
    bub_sorted = []
    bbub = []
    bbub_sorted = []
    for n in xs:
        a = list(range(n))
        bub_sorted.append(test(bubble_sort, a))
        bbub_sorted.append(test(better_bubble_sort, a))
        random.shuffle(a)
        bub.append(test(bubble_sort, a))
        bbub.append(test(better_bubble_sort, a))

    plt.plot(xs, bub, label = 'bubble')
    plt.plot(xs, bub_sorted, label = 'bubble sorted')
    plt.plot(xs, bbub, label = 'better bubble')
    plt.plot(xs, bbub_sorted, label = 'better bubble sorted')
    plt.legend()
    plt.xlabel('array size')
    plt.ylabel('time (sec)')
    plt.show()

### Programming 1 Tutorial ###

# ReCodEx: new homework

# Reminder: string splitting and joining, running time of list
# operations, nested lists.
#
# One thing to watch out for is list multiplication when creating
# lists of lists. If you do:
#
# >>> x = 3 * [3 * [0]]
# >>> x
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#
# It really seems like we got a 3 by 3 matrix. But the three rows
# of the matrix are shared!
#
# >>> x[0][0] = 1
# >>> x
# [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
#
# One way to solve this is for example:
#
# >>> x = [3 * [0] for _ in range(3)]
#
# We'll talk about this syntax later.
#
# Tuples are basically immutable lists. Immutability is sometimes useful
# (if we know we won't need the mutability, it can prevent silly bugs).
#
# In bigger programs, we often need to perform the same task multiple times.
# For example, we might want to sort two or more lists. While writing the
# sorting algorithm multiple times works, it's far from ideal. Apart from
# having to write the code multiple times, it will also create problems if we
# need to change the code (we found a bug, for example). We'd have to go through
# the entire program and fix each bit of code separately.
#
# In Python, we can solve this by defining functions. Once we have a function,
# we can simply call it multiple times. Functions can have parameters (essentially
# the input of the function), such as a list to be sorted or a number for primality
# checking. Functions can also produce some output. Inside the function, we can use
# a special return statement to specify what the output of the function is. Note
# that return exits the function, no other code after return is executed.
#
# When we assign to a variable inside a function, Python will create a new
# local variable, different from all the variables outside of the function (even
# if they have the same name). In general, it's good practice to only use local
# variables and parameters.

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

