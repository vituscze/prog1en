### Introduction to Algorithms Tutorial ###

# ReCodEx: homework solution + new homework

# Attendance: bonus points

# A bit of programming at the start: classes

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

import math

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



import math
import random

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def complete(h):
    if h == -1:
        return None

    left = complete(h - 1)
    right = complete(h - 1)
    return TreeNode(random.randrange(100), left, right)

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

# Write a function is_ancestor(p, q) that takes pointers to two nodes p and q in a binary tree
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
