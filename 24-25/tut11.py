### Introduction to Algorithms Tutorial ###

# ReCodEx: homework solution

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

# ReCodEx: homework solution

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

## Czech Flag ##

#  Write a Tkinter program that draws a Czech flag

import tkinter as tk

def flag(scale=200):
    root = tk.Tk()
    root.title('flag')

    canvas = tk.Canvas(root, width=6 * scale, height=4 * scale)
    canvas.grid()

    canvas.create_rectangle(0, 0, 6 * scale, 4 * scale, fill='#D7141A', width=0)
    canvas.create_rectangle(0, 0, 6 * scale, 2 * scale, fill='#FFFFFF', width=0)
    canvas.create_polygon(0, 0, 3 * scale, 2 * scale, 0, 4 * scale, fill='#11457E', width=0)

    root.mainloop()

## Drawing Lines ##

# Write a Tkinter program that lets the user draw lines. Initially the program should display
# a blank canvas. If the user clicks and drags the mouse, the program should display a line
# from the point where the user clicked to the current mouse position. When the user releases
# the mouse, the line should remain on the canvas. Each line should have a random color.

import random

class Scene:
    def __init__(self):
        self.edit_start = None
        self.edit_end = None
        self.edit_color = None

        self.lines = []

    def drawing(self):
        return self.edit_start is not None

    def draw_start(self, pos):
        assert self.edit_start is None, "already drawing a line"
        self.edit_start = pos
        self.edit_end = pos
        self.edit_color = f'#{random.randrange(1 << 24):06x}'

    def draw_end(self, pos):
        assert self.edit_start is not None, "not drawing a line"
        self.lines.append((self.edit_start, pos if pos else self.edit_end, self.edit_color))
        self.edit_start = None
        self.edit_end = None
        self.edit_color = None

    def draw_update(self, pos):
        assert self.edit_start is not None, "not drawing a line"
        self.edit_end = pos

BOARD_SIZE = 800

class View(tk.Canvas):
    def __init__(self, parent):
        self.scene = Scene()
        super().__init__(parent, width=BOARD_SIZE, height=BOARD_SIZE)
        self.grid()
        self.bind('<Button>', self.on_mousedown)
        self.bind('<ButtonRelease>', self.on_mouseup)
        self.bind('<Motion>', self.on_mousemove)
        self.draw()

    def draw_line(self, start, end, color):
        s_x, s_y = start
        e_x, e_y = end
        self.create_line(s_x, s_y, e_x, e_y, width=3, fill=color)

    def draw(self):
        self.delete('all')

        for line in self.scene.lines:
            self.draw_line(*line)

        if self.scene.drawing():
            self.draw_line(self.scene.edit_start, self.scene.edit_end, self.scene.edit_color)

    def on_mousedown(self, event):
        self.scene.draw_start((event.x, event.y))

    def on_mouseup(self, event):
        self.scene.draw_end((event.x, event.y))
        self.draw()

    def on_mousemove(self, event):
        if self.scene.drawing():
            self.scene.draw_update((event.x, event.y))
            self.draw()

def line_drawing():
    root = tk.Tk()
    root.title('line drawing')
    View(root)
    root.mainloop()
