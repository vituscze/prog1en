### Introduction to Algorithms Tutorial ###

# ReCodEx: new homework

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

### Programming 1 Tutorial ###

# ReCodEx: new homework

# Finishing "Same as the First" from last week.

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

## Date Class ##

# Write a class Date representing a month and day. The class should support these operations:
#
#     Date(m, d) – make a Date representing the given month (1 ≤ m ≤ 12) and day (1 ≤ d ≤ 31)
#
#     d.next() - return the Date after d
#
#     d.prev() - return the Date before d
#
#     d.add(n) – add n days to the given Date, wrapping past Dec 31 to Jan 1 if necessary
#
#     A Date object's string representation should look like this: "May 15".

DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

class Date:
    def __init__(self, m, d):
        assert 1 <= m <= 12, "Invalid month"
        assert 1 <= d <= DAYS_IN_MONTH[m - 1], "Invalid day"
        self.m = m
        self.d = d

    def __repr__(self):
        return f'{MONTHS[self.m - 1]} {self.d}'

    def _next_month(self):
        return 1 if self.m == 12 else self.m + 1

    def _prev_month(self):
        return 12 if self.m == 1 else self.m - 1

    def next(self):
        d = self.d + 1
        if d > DAYS_IN_MONTH[self.m - 1]:
            m = self._next_month()
            d = 1
        else:
            m = self.m
        return Date(m, d)

    def prev(self):
        d = self.d - 1
        if d < 1:
            m = self._prev_month()
            d = DAYS_IN_MONTH[m - 1]
        else:
            m = self.m
        return Date(m, d)

    def add(self, n):
        date = self
        for _ in range(n):
            date = date.next()
        return date
