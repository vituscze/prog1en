### Introduction to Algorithms Tutorial ###

# ReCodEx: homework solution + new homework

class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

def from_list(l):
    a = None
    for x in reversed(l):
        a = ListNode(x, a)
    return a

def to_list(a):
    result = []
    while a:
        result.append(a.val)
        a = a.next
    return result

# Split from the previous week
def split(n):
    a, b = None, None
    while n is not None:
        head = n
        n = n.next
        head.next = a
        a = head
        a, b = b, a
    return a, b

## Merge Lists ##

# Write a function merge() that takes pointer to the first Nodes of two sorted
# lists and combines them into a single sorted list.

def merge(a, b):
    if not a:
        return b
    if not b:
        return a

    c = None
    last = None

    while a and b:
        if a.val < b.val:
            smaller = a
            a = a.next
        else:
            smaller = b
            b = b.next
        if c is None:
            c = last = smaller
        else:
            last.next = smaller
            last = smaller
    if a:
        last.next = a
    if b:
        last.next = b
    return c

## Linked List Merge Sort ##

# Write a function merge_sort() that performs a merge sort on a linked list,
# returning a pointer to a sorted list. Do not allocate any new list nodes while sorting.

def merge_sort(ll):
    if ll is None or ll.next is None:
        return ll

    left, right = split(ll)
    left_s = merge_sort(left)
    right_s = merge_sort(right)
    return merge(left_s, right_s)

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

### Programming 1 Tutorial ###

# ReCodEx: homework solution + new homework

## Duplicate Values ##

# a) Write a function that takes a list of integers and returns True if there are any duplicate
# values in the list. Use sorting to accomplish this task. Do not modify the original list.

# b) Write a function with the same behavior, using a set to accomplish the task.

# c) Which implementation do you think will be faster on a large list in the best case? In the worst case?

# d) As an experiment, generate a list of random 1,000,000 integers in the range from 1 to 1,000,000,000,
# then call both of the above functions on your list. How does the exection time compare?

# e) Modify the experiment so that all the integers your generated list are unique. Now run both functions
# on your list. How does the execution time compare?

def has_duplicates_list(l):
    if len(l) <= 1:
        return False
    l = l.copy()
    l.sort()
    for i in range(len(l) - 1):
        if l[i] == l[i + 1]:
            return True
    return False

def has_duplicates_set(l):
    s = set()
    for x in l:
        if x in s:
            return True
        s.add(x)
    return False

def has_duplicates_set2(l):
    return len(l) != len(set(l))

import random
import time

def measure(f, x):
    t = time.time()
    f(x)
    return time.time() - t

def generate(count=1_000_000):
    return [random.randrange(1_000_000_000) for _ in range(count)]

def generate_unique(count=1_000_000):
    result = set()
    while len(result) < count:
        result.add(random.randrange(1_000_000_000))
    result = list(result)
    random.shuffle(result)
    return result

# >>> x = generate()
# >>> measure(has_duplicates_list, x)

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
