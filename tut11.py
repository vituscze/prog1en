### Introduction to Algorithms Tutorial ###

# ReCodEx: new homework

## Connected Maze ##

# Write a program that reads a rectangular maze from standard input in the following format,
# where '#' represents a wall:

########
# #  # #
# # #  #
#   # ##
##     #
########

# The maze will be surrounded by walls.

# The program should print True if the maze is connected, i.e. every two empty squares in the
# maze are connected by some path. Otherwise print False.

import sys

def mark_reachable(maze):
    def dfs(x, y):
        if maze[x][y] != ' ':
            return
        maze[x][y] = '.'
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            dfs(x + dx, y + dy)

    marked = False
    for x in range(len(maze)):
        for y in range(len(maze[x])):
            if maze[x][y] == ' ':
                if marked:
                    # We found an empty tile that wasn't
                    # reached by the earlier DFS.
                    return False
                else:
                    dfs(x, y)
                    marked = True
    return True

def read_maze():
    maze = []
    for line in sys.stdin:
        maze.append(list(line.strip()))
    return maze

## State Space Solver ##

# Write a function solve(start, goal, f) that can search any state space. solve()
# should take three arguments: a start state, a goal state, and a function f that
# computes the neighbors of any state. solve() should find the shortest possible path
# from the start state to the goal state, and should print out the sequence of states
# along this path, with one state per line. If no solution is possible, it should print
# 'no path'.

import collections

def bfs_list(start, goal, f):
    q = collections.deque()
    q.append([start])
    visited = {start}

    while len(q) > 0:
        l = q.popleft()
        if l[-1] == goal:
            return l
        for new_state in f(l[-1]):
            if new_state not in visited:
                q.append(l + [new_state])
                visited.add(new_state)

class Node:
    def __init__(self, state, prev=None):
        self.state = state
        self.prev = prev

def bfs(start, goal, f):
    q = collections.deque()
    q.append(Node(start))
    visited = {start}

    while len(q) > 0:
        node = q.popleft()
        if node.state == goal:
            return node
        for new_state in f(node.state):
            if new_state not in visited:
                q.append(Node(new_state, node))
                visited.add(new_state)

def solve(start, goal, f):
    node = bfs(start, goal, f)
    if node is None:
        print('no path')
        return
    path = []
    while node is not None:
        path.append(node.state)
        node = node.prev
    for s in reversed(path):
        print(s)

## Water Jugs ##

# We have three jugs with capacity 8, 5, and 3 liters. Initially the first
# jug is full of water, and the others are empty.

# We can pour water between the jugs, but they have no markings of any sort,
# so we can pour between two jars only until one of them becomes full or empty.

# What sequence of moves can we make so that the jugs will hold 4, 4, and 0
# liters of water, respectively?

# Write a program that can find the shortest possible sequence.

capacities = (8, 5, 3)
initial_state = (8, 0, 0)
final_state = (4, 4, 0)

def next_states(state):
    new_states = set()
    for start in range(len(state)):
        for end in range(len(state)):
            if start == end:
                continue
            amount = min(capacities[end] - state[end], state[start])
            if amount == 0:
                continue
            new_state = list(state)
            new_state[start] -= amount
            new_state[end] += amount
            new_states.add(tuple(new_state))
    return new_states

### Programming 1 Tutorial ###

# ReCodEx: new homework

## Expression Interpreter ##

# Write a program that reads and evaluates arithmetic expressions such as "22 + 31 - 4".
# In these expressions, the only supported arithmetic operators are "+" and "-", and parentheses
# are not allowed. Operators must be preceded and followed by writespace. Each time your program
# wants the user to enter an expression, it should print the prompt 'expr> ' and then wait for
# user input. The user can type 'exit' to exit the program. For example:

# expr> 2 + 3
# 5
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
# 5
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

## Location Class ##

# See: https://ksvi.mff.cuni.cz/~dingle/2023-4/prog_1/exercises_11.html

import math

EARTH_RADIUS = 6371

class InvalidLocation(Exception):
    pass

class Location:
    def __init__(self, lat, long):
        if not (-90 <= lat <= 90) or not (-180 <= long <= 180):
            raise InvalidLocation

        # There are a couple of locations that can be represented
        # in multiple ways. Pick some canonical representation to
        # make hashing/equality testing easier.
        if abs(lat) == 90: # Poles
            long = 0
        if long == -180: # Date line
            long = 180

        self.lat = lat
        self.long = long

    def __eq__(self, other):
        return isinstance(other, Location) and self.lat == other.lat and self.long == other.long

    def __hash__(self):
        return hash((self.lat, self.long))

    def __sub__(self, other):
        phi1, phi2, lam1, lam2 = map(lambda angle: angle * math.pi / 180, [self.lat, other.lat, self.long, other.long])

        # Haversine formula
        factor = math.sin(0.5 * (phi2 - phi1)) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(0.5 * (lam2 - lam1)) ** 2
        return 2 * EARTH_RADIUS * math.asin(math.sqrt(factor))
