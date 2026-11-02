### Introduction to Algorithms Tutorial ###

# ReCodEx: homework solution + new homework

# Attendance: bonus points

## Array Writes ##

# Suppose that we run a sorting algorithm on an array with N elements that is
# already sorted. How many array writes will it perform if we use each of the
# following algorithms?

# bubble sort
# selection sort
# insertion sort

def bubble_sort(a):
    writes = 0
    n = len(a)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                writes += 2
    return writes

def selection_sort(a):
    writes = 0
    n = len(a)
    for i in range(n - 1):
        min_index = i
        min_val = a[i]
        for j in range(i + 1, n):
            if a[j] < min_val:
                min_val = a[j]
                min_index = j
        # What if we check i != min_index?
        a[i], a[min_index] = a[min_index], a[i]
        writes += 2
    return writes

def insertion_sort(a):
    writes = 0
    n = len(a)
    for i in range(n):
        t = a[i]
        j = i - 1
        while j >= 0 and a[j] > t:
            a[j + 1] = a[j]
            writes += 1
            j -= 1
        a[j + 1] = t
        writes += 1
    return writes

## Binary Insertion ##

# Suppose that we run an insertion sort on an input array whose values are all 0 or 1. The array contains N values.
#
# a) What array of input values will be the worst case? What will be the worst-case running time?
#
# b) What will be the expected (i.e. average) running time, if the values in the input array are all randomly either 0 or 1?

# As we saw during the lecture, insertion sort is more efficient when the array is sorted, even partially.
# We expect the worse case to occur when the array is sorted the wrong way, i.e. ones followed by zeros.
#
# When we're in the middle of sorting and find a 1, we don't have to do anything (the sorted sequence at the
# start already ends with 1). When we find 0, we need to move all the 1s that were before it. So the worst
# arrangement clearly has to have all 1s in front of all 0s. The time it takes to sort is then given by
# number of ones (o) * number of zeros (z). We also know that z = n - o (amount of zeros and ones adds up to n).
# And as you might know, the expression o * (n - o) reaches its maximum value for o = n/2, giving us the time
# n^2/4. After adding the time required to visit each element, we get n^2/4 + n.
#
# On average, the i-th number will have i/2 ones in front of it. Because the number has 50% chance of being 1
# (requiring no work), i-th number will on average require i/4 operations. So we have 0/4 + 1/4 + ... + (n - 1)/4,
# which is (n^2 - n)/8. Final time is (n^2 - n)/8 + n, as before.

import itertools as it
import random

def find_max(n):
    return max([(insertion_sort(list(x)), x) for x in it.product([0,1], repeat=n)])

def gen_rand(n):
    return [random.randint(0,1) for _ in range(n)]

def avg_case(n, tries=10000):
    return sum([insertion_sort(gen_rand(n)) for _ in range(tries)]) / tries

## Selection Moves ##

# In a selection sort of an array with N elements, what is the maximum number of
# times that an element might move to a new position?

# In each step of selection sort, the minimum of the unsorted portion moves to
# the sorted portion. We need to find an array where swapping the head of the
# unsorted portion with the minimum leaves the other element in a position that's
# likely to get swapped again.

# Consider the array that's sorted except the maximum element is at the beginning:
#
#  a1 = [10,1,2,3,4,5,6,7,8,9]
#
# In the first step, we swap 1 and 10:
#
#  a2 = [1,10,2,3,4,5,6,7,8,9]
#
# Then we swap 2 and 10:
#
#  a3 = [1,2,10,3,4,5,6,7,8,9]
#
# Clearly the number 10 will be swapped 9 times (which is n - 1). Selection sort
# does a total of n - 1 swaps, we can't do better.

## Running Time ##

# Consider this function:
#
# def foo(n):
#     if n == 0:
#         return 0
#
#     return foo(n // 2) + foo(n // 2)
#
# a) For a given n, what value will the function compute?
#
# b) Write down a recurrence for T(N), the time to run the function foo(N).
#
# c) Solve the recurrence. Hint: Expand it into a tree as we did when we solved the recurrence for mergesort.
#
# d) Suppose that we change the last line to
#
# return 2 * foo(n // 2)
#
# Clearly this will not change the value that the function computes. Will this modification change its big-O running time?

# a) If the recursion stops, the result will always be zero, since the base case is always zero and the recursive
# case is just adding zeros together. However, since -1 // 2 == -1, the function doesn't work for negative numbers.
#
# b) T(N) = O(1) + 2 * T(N / 2)
#
# c) We know that T(N) = C + 2 * T(N / 2). We can draw the same tree we drew for mergesort. In the last layer, we have
# NC, in the layer above NC/2, then NC/4, etc. Adding them all up, we get (2N - 1)C, or O(N).
#
# d) The new recurrence is T(N) = O(1) + T(N / 2), giving us the time O(log N).

### Programming 1 Tutorial ###

# ReCodEx: homework solution + new homework

# Recursion is a programming technique where we define a function
# in terms of itself. It is generally used when we're trying to solve
# a problem that can be naturally split into smaller instances.
# A great example is the mergesort algorithm, where we need to
# sort two sublists of half the size and then merge them together.
#
# In Python, recursion tends to be fairly slow and has some
# further limitations compared to other languages. If you have
# a choice between iterative and recursive solutions, you should
# generally pick the iterative one.
#
# For a recursive solution to work, we need to handle the base case
# and the recursive case. The base case occurs the problem can be
# solved immediately (for example, when the length of a list is <= 1,
# it's trivially sorted). The recursive case works by solving one
# or more subproblems and using those results to compute the solution
# to the whole problem. When thinking about the recursive case, you can
# (should) assume the function already solves the subproblem. This is
# very similar to mathematical induction (and that's not a coincidence).

## No Zeroes, Recursively ##

# Write a function no_zeroes(n) that takes an integer n and returns an integer
# formed by removing all zeroes from the end of n's decimal representation. For example:

#  >>> no_zeroes(54000)
#  54
#  >>> no_zeroes(2256)
#  2256

# As a special case, no_zeroes(0) = 0.

# You may not use any loops in your solution, so you will need to write the function recursively.

def no_zeroes(n):
    if abs(n) > 9 and n % 10 == 0:
        return no_zeroes(n // 10)
    else:
        return n

## Recursive Power

# a) Write a recursive function is_pow_of_2(n) that returns True if n is a power of 2.
#
# b) Generalize the function: write a recursive function is_pow_of_k(k, n) that returns True if n is a power of k.

def is_pow_of_2(n):
    if n == 1:
        return True
    if n <= 0 or n % 2 != 0:
        return False
    else:
        return is_pow_of_2(n // 2)

def is_pow_of_k(k, n):
    if n == 1:
        return True
    if n <= 0 or n % k != 0:
        return False
    else:
        return is_pow_of_k(k, n // k)

## Same as the First ##

# Use recursion to write a function same_as_first(a) that returns the
# number of integers in an array a that are equal to its first element.

def same_as_first(a):
    if len(a) == 0:
        return 0

    first = a[0]

    def count(i):
        if i >= len(a):
            return 0
        elif a[i] == first:
            return 1 + count(i + 1)
        else:
            return count(i + 1)

    return count(0)

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

# What's the time complexity?
