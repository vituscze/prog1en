### Introduction to Algorithms Tutorial ###

# ReCodEx: homework solution + new homework

# How to tell if one algorithm is better than other? We express the number
# of steps taken by the program (and by step we mean some basic operation
# of the program, such as arithmetic operation, variable assignment, etc)
# as a function of the size of the input.
#
# However, for most programs these functions are going to be very messy
# and thus hard to compare. Instead, we approximate them by finding a
# nice approximation that serves at the upper bound (ideally smallest
# possible). We also typically only care about the asymptotic growth
# (how does the function behave as the size of the input goes to
# infinity) and for that we use the big-O notation.
#
# We say f(n) = O(g(n)) (sometimes we use set membership instead of the
# equal sign) when f(n)/g(n) approaches some finite number as n increases.
#
# For example, 2n = O(n), because 2n/n approaches 2. Similarly,
# n = O(n^2) because n/n^2 approaches 0. However, n != O(log n) because
# n/log n goes to infinity.

## Powers and Logs ##

# a) Is 2^(n+1) = O(2^n)?
#
# b) Is 2^(2n) = O(2^n)?
#
# c) Is log_2(n) = O(log_4(n))?

# Let's take a look at f(n)/g(n) and see what happens as we increase n.
# In a) we have 2^(n+1)/2^n, which can be simplified to just 2. f(n)/g(n)
# is thus always 2 no matter the value of n. And so 2^(n+1) = O(2^n).
#
# In b) we have 2^(2n)/2^n, which is 2^n. As n goes to infinity, so does
# 2^n. Thus 2^(2n) != O(2^n).
#
# In c) we have log_2(n)/log_4(n). Recall that log_4(n) = log_2(n)/2. We
# can simplify to 1/2 and thus log_2(n) = O(log_4(n)).

## Growth Rates ##

# Order these functions by increasing growth rate: n!, 2^n, n^10, n^log(n), 10^n, n^2.
#
# Let's start by writing down the trivial comparisons:
#
# 1) n^2 < n^10 < n^log(n)
# 2) 2^n < 10^n
#
# What's larger? n^log(n) or 2^n?
#
# n^log(n) = (2^log_2(n))^log(n) = 2^(log_2(n) * log(n)) which clearly grows slower than 2^n.
#
# We therefore have n^2 < n^10 < n^log(n) < 2^n < 10^n.
#
# Finally, what about n!? Let's consider n!/10^n:
#
#  1 *  2 *  3 *  4 * ... * 20 * 21 * ...    1    2         20
# --------------------------------------- = -- * -- * ... * -- * ...
# 10 * 10 * 10 * 10 * ... * 10 * 10 * ...   10   10         10
#
# The first 9 terms will give us a really small number, but after that
# we're multiplying by numbers >1. For large enough n, this will easily
# outdo the first 9 terms and give us arbitrarily large result.
#
# n^2 < n^10 < n^log(n) < 2^n < 10^n < n!

## Three ##

# Consider this program:

# n = int(input('Enter n: '))
#
# b = True
# while n > 1:
#     if n % 3 == 0:
#         n //= 3
#     else:
#         b = False
#         break
#
# print(b)

# a) For which values of n will it print 'True'?
#
# b) What is its best-case and worst-case big-O running time as a function of n?

# The program will print True if n <= 1 (it won't even enter the loop). If it
# does enter the loop, we keep dividing by 3 until we reach 1. If at any point
# the number isn't divisible by 3, we exit the loop and print False. For n > 1,
# True is only printed if n is a power of 3.
#
# Best case scenario is that n <= 1 where we only need O(1) steps. Similary for
# numbers that aren't divisible by 3. Worst case happens when n is a power of 3
# and we need to go through the entire cycle. Since we divide n by 3 in each
# iteration, we need at most log_3(n) iterations to reach 1 - O(log n) steps.

## Largest Prime Gap ##

# A prime gap is the difference between two consecutive prime numbers. For example,
# 7 and 11 are consecutive primes, and the gap between them has size 4.
#
# Write a program that reads an integer N ≥ 3 and prints the largest prime gap among
# primes that are less than N. The program should print the pair of consective primes
# along with the gap size.

import math

n = int(input())
sieve = (n + 1) * [True]
sieve[0] = sieve[1] = False

for i in range(2, math.isqrt(n) + 1):
    if sieve[i]:
        for j in range(i * i, n + 1, i):
            sieve[j] = False

primes = []
for i in range(n + 1):
    if sieve[i]:
        primes.append(i)

gap = 0
start = 0
end = 0
for i in range(len(primes) - 1):
    current = primes[i + 1] - primes[i]
    if current > gap:
        gap = current
        start = primes[i]
        end = primes[i + 1]

print('Largest gap:', gap)
print('Start:', start)
print('End:', end)

## Smallest Multiple ##

# Solve Project Euler's problem 5:
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math

n = 1
for i in range(1, 21):
    # Least common multiple
    n = n * i // math.gcd(n, i)
    # Also available as math.lcm
    # n = math.lcm(n, i)

print(n)

### Programming 1 Tutorial ###

# ReCodEx: homework solution + new homework

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

## Local and Global ##

# What will this program print?

a = 2
b = 3

def foo():
  a = b + 1
  a = a + 1
  return a

def bar():
  global b
  b = a + 3
  return b

def baz():
  return a + b

def thud():
  a = b + 1
  b = a + 1
  return a

print(foo())
print(bar())
print(baz())
print(thud())

# foo() returns 5, doesn't change the global a or b
# bar() returns 5, changes the global b to 5
# baz() returns 7, because b is now 5
# thud() is an error because b is a local variable and we're trying to use it
#   before it's initialized

## Lots of References ##

# Recall that a[:] makes a copy of the list a. It's the same as a[0:len(a)], or as a.copy().
#
# What will this program print? Why?

def bar(a):
    for i in range(len(a)):
        a[i] += 1
        a = a[:]

def foo(a):
    for b in a + a[:]:
        bar(b)
        bar(b[:])

m = [[1, 2], [3, 4]]
foo(m)

# Because bar replaces a with a copy after the first iteration of the loop,
# it only adds 1 to the first element of the list.
#
# Inside foo, the variable b goes over a[0], a[1], a[0] and a[1]. Notice that
# when going over a[:], we still access a[0] and a[1] -- this is because a[:]
# makes a SHALLOW copy. The first call of bar increments the first element of
# the list, as we established. The second call doesn't do anything interesting
# because the increment happens on a copy.
#
# The final result is thus [[3,2],[5,4]].

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
