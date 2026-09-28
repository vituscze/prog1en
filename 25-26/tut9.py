### Introduction to Algorithms Tutorial ###

# ReCodEx: homework solution (remove/count in detail) + new homework

## Heap Check ##

# Write a function that takes an array and returns True if the array represents a valid binary
# heap, otherwise False.

def is_min_heap(array):
    def go(i):
        if i >= len(array):
            return True

        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(array) and array[i] > array[left]:
            return False
        if right < len(array) and array[i] > array[right]:
            return False
        return go(left) and go(right)

    return go(0)

## Heap Positions ##

# Consider a binary min-heap that holds 12 values, with no duplicates.

# How many different array positions are possible for the second smallest value in the heap?

# How many different array positions are possible for the third smallest value in the heap?

# How many different array positions are possible for the fourth smallest value in the heap?

# How many different array positions are possible for the largest value in the heap?

# 2nd smallest value can be anywhere at depth 1; 3rd smallest anywhere at depths 1-2;
# 4th anywhere at depths 1-3; largest value can only be in leaves.


### Programming 1 Tutorial ###

# ReCodEx: homework solution + new homework + generating test data

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
# are not allowed. Operators must be preceded and followed by whitespace. Each time your program
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
