### Introduction to Algorithms Tutorial ###

# ReCodEx: homework solution + new homework

## Heap Check ##

# Write a function that takes an array and returns True if the array represents a valid binary
# heap, otherwise False.

def is_min_heap(array):
    last = len(array) - 1
    last_parent = (last - 1) // 2
    for i in range(last_parent + 1): # no need to check elements with no children
        left  = 2 * i + 1
        right = 2 * i + 2
        if left <= last and array[i] > array[left]: # the left <= last condition technically isn't necessary
            return False
        if right <= last and array[i] > array[right]:
            return False
    return True

## Heap Positions ##

# Consider a binary min-heap that holds 12 values, with no duplicates.

# How many different array positions are possible for the second smallest value in the heap?

# How many different array positions are possible for the third smallest value in the heap?

# How many different array positions are possible for the fourth smallest value in the heap?

# How many different array positions are possible for the largest value in the heap?

# 2nd smallest value can be anywhere at depth 1; 3rd smallest anywhere at depths 1-2;
# 4th anywhere at depths 1-3; largest value can only be in leaves.

## Adjacency Matrix to Adjacency List ##

# Write a function that takes a undirected graph in adjacency matrix representation, and returns
# the same graph in adjacency list representation. Assume that the graph's vertices are numbered
# from 0 to (V – 1).

def to_adj_list(m):
    v = len(m)
    l = [[] for _ in range(v)]
    for i in range(v):
        for j in range(v):
            if m[i][j]:
                l[i].append(j)
    return l

## Adjacency List to Adjacency Matrix ##

# Write a function that takes a undirected graph in adjacency list representation, and returns
# the same graph in adjacency matrix representation. Assume that the graph's vertices are numbered
# from 0 to (V – 1).

def to_adj_matrix(l):
    v = len(l)
    m = [v * [False] for _ in range(v)]
    for i, edges in enumerate(l):
        for j in edges:
            m[i][j] = True
    return m

## Reverse the Direction ##

# Write a functon that takes a directed graph G in adjacency list representation, with integer vertex
# ids. The function should return a graph that is like G, but in which all edges point in the opposite
# direction.

def reverse_graph(l):
    v = len(l)
    new_l = [[] for _ in range(v)]
    for i, edges in enumerate(l):
        for j in edges:
            new_l[j].append(i)
    return new_l

## Mutually Reachable ##

# Write a function that takes a directed graph in adjacency list representation and two integer vertex
# ids v and w.The function should return True if v and w are mutually reachable, i.e. there is some path
# from v to w and also from w to v. Use one or more depth-first searches.

def reachable(graph, v, w):
    visited = [False for _ in graph]

    def visit(u):
        if u == w:
            return True
        visited[u] = True
        for n in graph[u]:
            if not visited[n] and visit(n):
                return True
        return False

    return visit(v)

def mutually_reachable(graph, v, w):
    return reachable(graph, v, w) and reachable(graph, w, v)

## Directed Acyclic Graph ##

# Suppose that we run a depth-first search on a directed acyclic graph, i.e. a directed graph with no cycles.
# And suppose that we omit the visited set from our implementation. It might look like this:

def dfs(graph, start):
    def visit(v):
        print('visiting', v)
        for w in graph[v]:
            visit(w)

    visit(start)

# Is the search guaranteed to terminate, or might it go into an infinite loop? If it will terminate,
# is the search guaranteed to run in O(V + E)?

# Because the graph is acyclic, we definitely won't go into an infinite loop. However, we will most
# likely visit the same vertices multiple times. On really degenerate graphs, this can lead to
# exponential slowdown.

def generate(n, ix=0):
    if n == 0:
        return [[]]
    return [[ix + 1, ix + 2], [ix + 3], [ix + 3]] + generate(n - 1, ix + 3)

def dfs_quiet(graph, start):
    def visit(v):
        for w in graph[v]:
            visit(w)

    visit(start)

import time
import matplotlib.pyplot as plt

def time_dfs(n):
    t1 = time.time()
    dfs_quiet(generate(n), 0)
    t2 = time.time()
    return t2 - t1

def plot():
    xs = list(range(20))
    dfs_data = list(map(time_dfs, xs))

    plt.plot(xs, dfs_data, label='bad dfs')
    plt.legend()
    plt.xlabel('size')
    plt.ylabel('time (sec)')
    plt.show()

### Programming 1 Tutorial ###

# ReCodEx: homework solution + new homework

## Exception Performance ##

# How expensive are exceptions? To find out, perform the following experiment. Consider the following functions
# square1() and square2(). Both of them return the square of a value, but sqaure1() returns the square normally,
# while square2() throws it in an exception:

def square1(x):
    return x * x

class Answer(Exception):
    def __init__(self, x):
        self.x = x

def square2(x):
    raise Answer(x * x)

# Write a program that adds the squares of the numbers from 1 to 10,000,000 in two ways, first by calling square1(),
# then by calling square2() and using a try...except block. Use the time.time() function to measure the total cost
# of adding these squares in each of these ways.

import time

def measure(f):
    t1 = time.time()
    f()
    t2 = time.time()
    return t2 - t1

def first():
    total = 0
    for i in range(10_000_000):
        total += square1(i)
    return total

def second():
    total = 0
    for i in range(10_000_000):
        try:
            square2(i)
        except Answer as a:
            total += a.x
    return total

# >>> measure(first)
# 0.9119935035705566
# >>> measure(second)
# 3.998006582260132

## Expression Interpreter ##

# Write a program that reads and evaluates arithmetic expressions such as "22 + 31 - 4".
# In these expressions, the only supported arithmetic operators are "+" and "-", and parentheses
# are not allowed. Operators must be preceded and followed by writespace. Each time your program
# wants the user to enter an expression, it should print the prompt 'expr> ' and then wait for
# user input. The user can type 'exit' to exit the program. For example:

# expr> 2 + 3
# 7
# expr> 1 + 22 – 3
# 20
# expr> exit

# Your program should include a function eval() that takes a string containing an arithmetic expression
# and returns its value. If an expression is invalid (e.g. it contains a value that is not an integer,
# or includes an unsupported operator such as '*') then eval() should raise a InvalidExpression exception,
# which is a custom exception type that you should define. If an InvalidExpression exception is raised,
# then your program's top-level code should catch it, print an error message, then continue execution,
# prompting the user for the next expression. For example:

# expr> 2 + 3
# 7
# expr> 5 + b
# Invalid expression
# expr> 7 * 2
# Invalid expression
# expr> exit

class InvalidExpression(Exception):
    pass

def parse_int(s):
    try:
        return int(s)
    except ValueError:
        raise InvalidExpression

def eval(s):
    split = s.split()
    if len(split) % 2 != 1:
        raise InvalidExpression
    result = parse_int(split[0])
    for i in range(1, len(split), 2):
        val = parse_int(split[i + 1])
        op = split[i]
        if op == '+':
            result += val
        elif op == '-':
            result -= val
        else:
            raise InvalidExpression
    return result

def main():
    while True:
        line = input('expr> ')
        if line == 'exit':
            break
        try:
            print(eval(line))
        except InvalidExpression:
            print('Invalid expression')

## Monotonic Search ##

# Write a function search(f, y, lo, hi, epsilon) takes a function f of a single variable, plus values y, lo, hi
# and epsilon. The function f is guaranteed to be monotonic, i.e. f(x1) < f(x2) whenever x1 < x2. The function
# should find some value x in the range lo ≤ x ≤ hi such that |f(x) – y| <= epsilon. The function should return x,
# or None if there is no such value within the given range lo .. hi. Hint: Use a binary search.

def search(f, y, lo, hi, epsilon):
    if y < f(lo) - epsilon:
        return
    if y > f(hi) + epsilon:
        return

    while True:
        mid = (lo + hi) / 2
        f_mid = f(mid)
        if abs(f_mid - y) <= epsilon:
            return mid
        if y < f_mid:
            hi = mid
        else:
            lo = mid

## Stream Classes ##

# Write a class Stream for reading lines of text, with subclasses StringStream and FileStream.
# Stream will be an abstract class: it does not make sense to create an instance of Stream,
# only of one of its subclasses.

# On any Stream, it should be possible to call a method next_line() that reads the next input line
# and returns it as a string, or returns None at the end of the input. There should be a constructor
# StringStream(s) that takes a string containing data to read, and a constructor FileStream(name)
# that builds a FileStream that will read data from the given file. You will have separate implementations
# of next_line() in each of these subclasses.

# The Stream class should also have a method next_non_empty() that reads lines until it finds a line that
# it non-empty, then returns it. If there are no more non-empty lines, the method should return None. You
# will need to implement this method only once.

from abc import ABC, abstractmethod

class Stream(ABC):
    @abstractmethod
    def next_line(self):
        pass

    def next_non_empty(self):
        while (l := self.next_line()) == '':
            pass

        return l

class FileStream(Stream):
    def __init__(self, path):
        self.file = open(path)

    def next_line(self):
        l = self.file.readline()
        return None if l == '' else l.strip('\n')

class StringStream(Stream):
    def __init__(self, string):
        self.data = string.split('\n')
        self.pos = 0

    def next_line(self):
        if self.pos + 1 >= len(self.data):
            return None
        self.pos += 1
        return self.data[self.pos - 1]
