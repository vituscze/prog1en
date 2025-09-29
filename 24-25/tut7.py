### Introduction to Algorithms Tutorial ###

# ReCodEx: homework solution + new homework

## Incomplete Partitioning ##

# Consider the Hoare partitioning function for quicksort that we saw in the lecture:

import random

def partition(a, lo, hi):
    p = a[random.randrange(lo + 1, hi)]  # choose random pivot

    i = lo
    j = hi - 1

    while True:
        # Look for two elements to swap.
        while a[i] < p:
            i += 1
        while a[j] > p:
            j -= 1

        if j <= i:             # nothing to swap
            return i

        # print(f'swapping {i} and {j}')
        a[i], a[j] = a[j], a[i]
        # i += 1
        # j -= 1

# Suppose that we remove the last two lines from the function above.
# Show that the function will no longer behave correctly with this change.
# Specifically, give an example of an input array on which the function will fail.

# The inner while cycles might not even run once, letting us swap the same
# two positions forever. For example:

# paratition(4 * [0], 0, 4)

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

## Merge Sort Memory ##

# Consider the merge sort implementation that we saw in the lecture.

# a) If we use it to sort an array that occupies N bytes of memory, what is the
# largest amount of additional memory that will be required at any moment during
# the sorting process? (Assume that any temporary arrays are freed as soon as
# there are no more references to them.)

# b) Is it possible to modify our implementation to reduce this memory requirement?

# Merge sorted arrays a and b into c, given that
# len(a) + len(b) = len(c).
def merge(a, b, c):
    i = j = 0     # index into a, b

    for k in range(len(c)):
        if j == len(b):      # no more elements available from b
            c[k] = a[i]      # so we take a[i]
            i += 1
        elif i == len(a):    # no more elements available from a
            c[k] = b[j]      # so we take b[j]
            j += 1
        elif a[i] < b[j]:
            c[k] = a[i]      # take a[i]
            i += 1
        else:
            c[k] = b[j]      # take b[j]
            j += 1

extra_memory = 0
max_memory = 0
def merge_sort(a):
    global extra_memory, max_memory
    if len(a) < 2:
        return

    mid = len(a) // 2

    left = a[:mid]      # copy of left half of array
    right = a[mid:]     # copy of right half
    extra_memory += len(a)  # we had to copy len(a) elements
    if extra_memory > max_memory:
        max_memory = extra_memory

    merge_sort(left)
    merge_sort(right)

    merge(left, right, a)
    # left and right arrays are no longer needed at this point
    extra_memory -= len(a)

# It takes log(n) steps to reach the base case of the recursion. Once there,
# we have 2 additional lists at every level. The first ones have length n/2
# (a total of n), the second ones n/4 (a total of n/2) and so on. If we sum
# all of these, we get ~2n.

# Do we need that much memory? Notice that the only reason we need the extra
# memory is because we cannot merge in-place. However, after we merge the lists
# a and b into c, we no longer need to preserve the original lists and we can
# simply reuse them in the next merge.

def merge_better(source, target, start_a, end_a, start_b, end_b, start_c, end_c):
    assert (end_a - start_a) + (end_b - start_b) == (end_c - start_c)
    i = start_a
    j = start_b

    for k in range(start_c, end_c):
        if j == end_b:                 # no more elements available from b
            target[k] = source[i]      # so we take a[i]
            i += 1
        elif i == end_a:               # no more elements available from a
            target[k] = source[j]      # so we take b[j]
            j += 1
        elif source[i] < source[j]:
            target[k] = source[i]      # take a[i]
            i += 1
        else:
            target[k] = source[j]      # take b[j]
            j += 1

def merge_sort_better(a):
    def helper(source, target, start, end):
        range_len = end - start
        if range_len == 0:
            return
        if range_len == 1:
            target[start] = source[start]
            return

        mid = (start + end) // 2
        helper(target, source, start, mid)
        helper(target, source, mid, end)
        merge_better(source, target, start, mid, mid, end, start, end)

    helper(a[:], a, 0, len(a))

### Programming 1 Tutorial ###

# ReCodEx: homework solution + new homework

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

## Split a List ##

# Write a function split() that takes a pointer to the the first Node in a linked list
# and splits the list into two linked lists of roughly equal size. Return a pair containing
# these lists. The elements in the returned lists may appear in any order.

def split(n):
    a, b = None, None

    while n is not None:
        # Remove head of n
        head = n
        n = n.next
        # Add head to a
        head.next = a
        a = head
        # Swap a and b
        # This ensures that we're not adding new
        # elements to only one of the lists.
        a, b = b, a

    return a, b
