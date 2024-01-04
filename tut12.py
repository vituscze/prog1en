### Introduction to Algorithms Tutorial ###

class Expr:
    pass

class IntExpr(Expr):
    def __init__(self, val):
        self.val = val

    def eval(self):
        return self.val

    def to_infix(self):
        return str(self.val)

class OpExpr(Expr):
    def __init__(self, op, left, right):
        self.op = op
        self.left, self.right = left, right

    def eval(self):
        l = self.left.eval()
        r = self.right.eval()
        if self.op == '+': return l + r
        if self.op == '-': return l - r
        if self.op == '*': return l * r
        if self.op == '/': return l // r
        if self.op == '_': assert False

    def to_infix(self):
        return f'({self.left.to_infix()} {self.op} {self.right.to_infix()})'

class Lexer:
    def __init__(self, s):
        self.s = s
        self.i = 0    # position of next token

    # Read and return the next token (an int or a char),
    # or return None if there are no more.
    def next(self):
        # move past spaces
        while self.i < len(self.s) and self.s[self.i] == ' ':
            self.i += 1

        if self.i >= len(self.s):
            return None

        c = self.s[self.i]
        self.i += 1
        if c.isdigit():   # start of an integer constant
            t = c
            while self.i < len(self.s) and self.s[self.i].isdigit():
                t += self.s[self.i]
                self.i += 1
            return int(t)

        assert c in '+-*/()', 'invalid character'
        return c

def parse_infix(s):
    reader = Lexer(s)

    # Parse a subexpression starting at the current point.
    def parse():
        t = reader.next()
        if isinstance(t, int):
            return IntExpr(t)

        assert t == '(', 'expected ('
        left = parse()

        op = reader.next()
        assert op in '+-*/', 'invalid operator'

        right = parse()
        assert reader.next() == ')', 'expected )'

        return OpExpr(op, left, right)

    return parse()

## Expressions with Variables ##

# Extend the infix expression parser from the lecture so that an expression can contain variables,
# where every variable name is a lowercase letter. For example, here is one possible expression:

# ((2 + x) * (y – 7))

# Also extend the eval() function so that it can evaluate an expression with variables, given
# a dictionary that maps each variable name to its value.

class Expr:
    pass

class IntExpr(Expr):
    def __init__(self, val):
        self.val = val

    # First change: eval has a context (dictionary) that specifies each variable's value
    def eval(self, ctx):
        return self.val

    def to_infix(self):
        return str(self.val)

class OpExpr(Expr):
    def __init__(self, op, left, right):
        self.op = op
        self.left, self.right = left, right

    def eval(self, ctx):
        l = self.left.eval(ctx)
        r = self.right.eval(ctx)
        if self.op == '+': return l + r
        if self.op == '-': return l - r
        if self.op == '*': return l * r
        if self.op == '/': return l // r
        if self.op == '_': assert False

    def to_infix(self):
        return f'({self.left.to_infix()} {self.op} {self.right.to_infix()})'

# Second change: new subclass representing variable expressions
class VarExpr(Expr):
    def __init__(self, name):
        self.name = name

    # The context contains information about variables' values;
    # simply look up the value of our variable.
    def eval(self, ctx):
        return ctx[self.name]

    def to_infix(self):
        return self.name

class Lexer:
    def __init__(self, s):
        self.s = s
        self.i = 0    # position of next token

    # Read and return the next token (an int or a char),
    # or return None if there are no more.
    def next(self):
        # move past spaces
        while self.i < len(self.s) and self.s[self.i] == ' ':
            self.i += 1

        if self.i >= len(self.s):
            return None

        c = self.s[self.i]
        self.i += 1
        if c.isdigit():  # start of an integer constant
            t = c
            while self.i < len(self.s) and self.s[self.i].isdigit():
                t += self.s[self.i]
                self.i += 1
            return int(t)

        # Third change: lexer supports variable names
        if c.isalpha():  # start of a variable name
            t = c
            while self.i < len(self.s) and self.s[self.i].isalpha():
                t += self.s[self.i]
                self.i += 1
            return t

        assert c in '+-*/()', 'invalid character'
        return c

def parse_infix(s):
    reader = Lexer(s)

    # Parse a subexpression starting at the current point.
    def parse():
        t = reader.next()
        if isinstance(t, int):
            return IntExpr(t)
        # Fourth change: if lexer gives us an identifier, create a variable expression
        if t.isalpha():
            return VarExpr(t)

        assert t == '(', 'expected ('
        left = parse()

        op = reader.next()
        assert op in '+-*/', 'invalid operator'

        right = parse()
        assert reader.next() == ')', 'expected )'

        return OpExpr(op, left, right)

    return parse()

# >>> e = parse_infix('((2 + 3) * (x + y))')
# >>> e.eval({'x':1, 'y':10})
# 55

## Expression Simplification ##

# Extending the previous exercise, write a function simplify() that takes an expression tree
# and simplifies it by making the following replacements:

# E + 0 => E

# 0 + E => E

# E * 0 => 0

# 0 * E => 0

# E * 1 => E

# 1 * E => E

# For example, simplifying the expression '((x * 1) + (y * 0))' will yield the expression 'x'.

def simplify(expr):
    if isinstance(expr, OpExpr):
        l_simple = simplify(expr.left)
        r_simple = simplify(expr.right)

        def is_val(e, v):
            return isinstance(e, IntExpr) and e.val == v

        if expr.op == '+' and is_val(l_simple, 0):
            return r_simple
        if expr.op == '+' and is_val(r_simple, 0):
            return l_simple
        if expr.op == '*' and (is_val(l_simple, 0) or is_val(r_simple, 0)):
            return IntExpr(0)
        if expr.op == '*' and is_val(l_simple, 1):
            return r_simple
        if expr.op == '*' and is_val(r_simple, 1):
            return l_simple

        return OpExpr(expr.op, l_simple, r_simple)
    else:
        return expr

### Programming 1 Tutorial ###

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
