### Introduction to Algorithms Tutorial ###

# ReCodEx: homework solution + new homework

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



import math
import random

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def complete(h):
    if h == -1:
        return None

    left = complete(h - 1)
    right = complete(h - 1)
    return Node(random.randrange(100), left, right)

def print_tree(n, depth=0):
    if n is not None:
        print_tree(n.left, depth + 1)
        print(depth * '  ', n.val)
        print_tree(n.right, depth + 1)

## Mirror Image ##

# Write a function mirror(t) that modifies a binary tree, flipping it
# from left to right so that it looks like a mirror image of the original tree.

def mirror(t):
    if t is not None:
        mirror(t.left)
        mirror(t.right)
        t.left, t.right = t.right, t.left

## Maximum Value ##

# a) Write a function max_in_tree(t) that returns the maximum value in any binary tree.

# b) Modify the function to be more efficient if the input tree is known to be a binary search tree.

def max_in_tree(t):
    if t is None:
        return -math.inf
    else:
        return max(t.val, max_in_tree(t.left), max_in_tree(t.right))

def max_in_bst(t):
    if t is None:
        return -math.inf
    else:
        while t.right is not None:
            t = t.right
        return t.val

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
