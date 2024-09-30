### Introduction to Algorithms Tutorial ###

# ReCodEx: new homework

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

# a) It will always be zero, since the base case is always zero and the recursive case is just adding zeros together.
#
# b) T(N) = O(1) + 2 * T(N / 2)
#
# c) We know that T(N) = C + 2 * T(N / 2). We can draw the same tree we drew for mergesort. In the last layer, we have
# NC, in the layer above NC/2, then NC/4, etc. Adding them all up, we get (2N - 1)C, or O(N).
#
# d) The new recurrence is T(N) = O(1) + T(N / 2), giving us the time O(log N).

### Programming 1 Tutorial ###

# ReCodEx: new homework

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

## Local and Global ##

# What will this program print?

# a = 2
# b = 3
#
# def foo():
#   a = b + 1
#   a = a + 1
#   return a
#
# def bar():
#   global b
#   b = a + 3
#   return b
#
# def baz():
#   return a + b
#
# def thud():
#   a = b + 1
#   b = a + 1
#   return a
#
# print(foo())
# print(bar())
# print(baz())
#
# print(thud())

# foo() first stores 4 into a (using the global b), then adds 1 more to it. Result is 5,
# global a and b are unchanged. bar() stores 5 (using the global a) into global b.
# Result is 5 again but this time the global b has been changed to 5. baz() adds
# global a and b together, returning 7. thud() produces an error because it's trying
# to access local b before it was defined.

## No Zeroes, Recursively ##

# Write a function no_zeroes(n) that takes an integer n and returns an integer
# formed by removing all zeroes from the end of n's decimal representation. For example:

# no_zeroes(54000)
# 54
# no_zeroes(2256)
# 2256

# As a special case, no_zeroes(0) = 0.
#
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

## Lots of References ##

# Recall that a[:] makes a copy of the list a. It's the same as a[0:len(a)], or as a.copy().

# What will this program print? Why?

# def bar(a):
#     for i in range(len(a)):
#         a[i] += 1
#         a = a[:]
#
# def foo(a):
#     for b in a + a[:]:
#         bar(b)
#         bar(b[:])
#
# m = [[1, 2], [3, 4]]
# foo(m)
# print(m)

# The first loop we go through (in the function foo) operates on
# the list m and a copy of m. But because the copy is shallow (i.e.
# it only copies the outer list, it doesn't copy the elements),
# it still refers to lists m[0] ([1,2]) and m[1] ([3,4]).
#
# Before we jump to bar(b), we can easily determine what happens with
# bar(b[:]). This function operates on copies of m[0] and m[1] and thus
# cannot have any effect on m[0] and m[1] themselves. We can safely ignore it.
#
# That leaves us with bar(b). It will be called 4 times, on m[0], m[1], m[0]
# and m[1] (in this order). Inside the bar function, we start by incrementing
# the first element of the list (m[0] or m[1]), then we create a copy of it
# and after that it doesn't matter what we do because we've lost access to
# the m[0] and m[1] lists. Because bar is called twice on each of m[0] and m[1],
# it means the increment of the first element will be done twice.
#
# We expect the result to be [[3,2],[5,4]]

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
print(m)
