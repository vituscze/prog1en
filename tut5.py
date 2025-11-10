### Introduction to Algorithms Tutorial ###

# ReCodEx: homework solution + new homework

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

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Return the distance from this point to the origin.
    def from_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    # Return true if this point is the origin (0, 0).
    def is_origin(self):
        d = self.from_origin()
        return d == 0

    # Return the distance between this point and another point q.
    def distance(self, q):
        return math.sqrt((self.x - q.x) ** 2 + (self.y - q.y) ** 2)

## Circle Class ##

# Write a class Circle representing a circle in 2 dimensions. The class should support these operations:
#
#     Circle(p, r) – make a circle whose center is at p, with radius r
#
#     c.area() - return the area of a circle
#
#     c.circumference() – return the circumference of a circle
#
#     c.contains(p) – return true if point p is inside the circle c

class Circle:
    def __init__(self, p, r):
        assert r >= 0, 'Negative radius'
        self.p = p
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

    def circumference(self):
        return 2 * math.pi * self.r

    def contains(self, p):
        return self.p.distance(p) <= self.r

## Adjacent Elements ##

# We can use this class to represent a linked list node:

class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

# Write a function has_adjacent(n) that takes a pointer to the first Node in a linked list
# and returns True if any two adjacent elements in the list have the same value, otherwise False.

def from_list(l):
    head = None
    for x in reversed(l):
        head = Node(x, head)
    return head

def has_adjacent(n):
    # Linked lists of length 0 or 1 cannot have adjacent elements.
    if n is None or n.next is None:
        return False

    # While we have at least two elements remaining
    while n.next is not None:
        if n.val == n.next.val:
            return True
        n = n.next

    return False

## Prepend ##

# You are given a class LinkedList with an attribute head that points to the head of a linked list of Node objects:

class LinkedList:
    def __init__(self, head):
        self.head = head

# Write a method that prepends a value to a LinkedList.

    def prepend(self, x):
        # Create a new head node that points to the original head
        self.head = Node(x, self.head)

# We'll also define a method to print the linked list to make it easier
# to see what's going on.

    def print(self):
        n = self.head
        while n is not None:
            print(n.val, end=' ')
            n = n.next
        print()

## Append ##

# Write a method that appends a value to a LinkedList.

    def append(self, x):
        # When the linked list is empty, it's the same
        # as prepending an element
        if self.head is None:
            self.head = Node(x, None)
        # Otherwise, if we only have access to head, we first need
        # to go through the linked list and find the last element
        last = self.head
        while last.next is not None:
            last = last.next
        # At this point we have the last element and we can add
        # a new node after it
        last.next = Node(x, None)

## Delete First ##

# Write a method that deletes the first node (if any) in a LinkedList.

    def delete_first(self):
        if self.head is not None:
            self.head = self.head.next

## Comparing Dictionaries ##

# Write a function same_dict(d1, d2) that returns true if two dictionaries have
# the same key-value pairs. You may not use the == method to compare the
# dictionaries directly (though you may use == on other types in your solution).
# For example:

#  >>> same_dict({ 10 : 20, 30 : 40 }, { 30 : 40, 10 : 20 })
#  True

# If the two dictionaries have a total of N elements, what will be your function's
# expected big-O running time?

def same_dict(d1, d2):
    if len(d1) != len(d2):
        return False
    for k, v in d1.items():
        if k not in d2:
            return False
        if v != d2[k]:
            return False
    return True
