### Introduction to Algorithms Tutorial ###

# ReCodEx: new homework

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

## Recursive Tree ##

# Write a class TreeSet that implements a set of values using a binary search tree,
# with methods add() and contains(). Implement these methods using recursion, with no
# loops. Hint: write recursive helper functions outside your TreeSet class that work
# with Node objects.

def tree_add(root, x):
    if root is None:
        return Node(x)
    else:
        if x < root.val:
            root.left = tree_add(root.left, x)
        elif x > root.val:
            root.right = tree_add(root.right, x)
        return root

def tree_contains(root, x):
    if root is None:
        return False
    else:
        if x < root.val:
            return tree_contains(root.left, x)
        elif x > root.val:
            return tree_contains(root.right, x)
        else:
            return True

class TreeSet:
    def __init__(self):
        self.root = None

    def add(self, x):
        self.root = tree_add(self.root, x)

    def contains(self, x):
        return tree_contains(self.root, x)

## Tree Check ##

# Write a function that takes a binary tree and returns True if the tree satisfies
# the ordering requirements of a binary search tree.

def tree_check(root, lo=-math.inf, hi=math.inf):
    if root is None:
        return True
    elif lo < root.val < hi:
        return tree_check(root.left, lo, root.val) and tree_check(root.right, root.val, hi)
    else:
        return False

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

# ReCodEx: new homework

# Upcoming deadline for project proposals!

# Sets and dictionaries
#
# Set is a collection of unique items (just like in mathematics). Internally, sets are
# implemented as hash tables. The details are not important (yet), but there are two
# consequences for us: if you want to put something into a set (or a dictionary), it
# must support equality comparison (__eq__) and a special hash function (__hash__).
#
# The main advantage of sets is that checking if something is in a set can be
# done in O(1) on average.
#
# >>> s = set() # empty set
# >>> s.add(5) # inserting a new element
# >>> s
# {5}
# >>> s.add(5) # duplicates are ignored
# >>> s
# {5}
# >>> s = {1,2,3} # sets can also be created like lists
# >>> s.remove(2)
# >>> s
# {1, 3}
# >>> s.remove(2) # cannot remove an element that isn't present
# KeyErorr: 2
# >>> {1,2} | {2,3} # set union
# {1, 2, 3}
# >>> {1,2} & {2,3} # set intersection
# {2}
# >>> {c for c in 'hello there'} # unique letters
# {'t', 'e', 'r', 'l', 'o', 'h', ' '}
#
# Like a set, a dictionary is a collection of unique keys. However, each key also
# has an associated value. It is also implemented as a hash table, which means that
# keys (but not values) need to support equality comparison and a hash function.
#
# Like a set, we can quickly check if a key is present in the dictionary, but we
# can also quickly access or change the associated value.
#
# >>> d = {} # empty dictionary
# >>> d['hello'] = 5 # inserting a new key-value pair
# >>> d
# {'hello': 5}
# >>> 'hello' in d # checking if a key is present
# True
# >>> d['hello'] # accessing the associated value
# 5
# >>> del d['hello'] # removing a key and its value
# >>> d
# {}

## Duplicate Letters ##

# Write a function has_dups(s) that takes a string and returns True if the string
# has any duplicate letters. The string may contain any Unicode characters such as 'λ' or 'ř'.

def has_dups(s):
    counts = {}
    for c in s:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    for k, v in counts.items():
        if v > 1:
            return True
    return False

## Unique Word Count ##

# Write a program that reads text from standard input until it ends,
# and prints the number of unique words in the input.

import sys

def word_count(f):
    words = set()
    for line in f:
        for word in line.lower().split():
            words.add(word)
    print(len(words))

# word_count(sys.stdin)

## Combining Dictionaries ##

# Write a function combine(d, e) that takes two dictionaries. It should return a
# dictionary that maps x to z if d maps x to some y, and e maps y to z. For example,
# suppose that d is a dictionary that maps Czech words to English words, and e maps
# English words to Spanish words:

d = { 'žába' : 'frog', 'kočka' : 'cat', 'kráva' : 'cow' }
e = { 'cow' : 'vaca', 'cat' : 'gato', 'dog' : 'perro' }

# Then combine(d, e) will map Czech to Spanish:

# combine(d, e)
# {'kočka': 'gato', 'kráva': 'vaca'}

# Notice that 'žába' is not a key in the resulting dictionary, since e doesn't map 'frog'
# to anything. Similarly, 'perro' is not a value in the resulting dictionary, since d doesn't
# map anything to 'dog'.

def combine(dict1, dict2):
    d = {}
    for key1, val1 in dict1.items():
        if val1 in dict2:
            d[key1] = dict2[val1]
    return d

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
