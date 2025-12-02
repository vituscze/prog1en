### Introduction to Algorithms Tutorial ###

# ReCodEx: homework solution + new homework

## Modular Hashing ##

# Consider the hash function we saw in the lecture:

B = 0

# Generate a hash code in the range 0 .. 2^32 - 1.
def my_hash(s):
    h = 0
    for c in s:
        d = ord(c)
        h = (B * h + d) % (2 ** 32)
    return h

# a) If B = 0, what hash function will result? Will this be a good hash function?

# b) If B = 1, what hash function will result? Will this be a good hash function?

# c) Suppose that we want to place all unique words of War and Peace into 10,000
# hash buckets. If we use the hash function above, some values of B will be better
# than others, because they will result in a more even distribution of hash values.
# Design an experiment to compare the performance of these choices: B = 2; B = 256;
# B = 257; B = 65,537; B = 1,000,003.

# for B = 0, we have:

# >>> my_hash('a') == my_hash('aha') == my_hash('banana')
# True

# That is, the hash is only using the last letter. For lower-case words,
# this means that the hash would only ever fill a maximum of 26 buckets.
# B = 1 is a bit better, but still not great:

# >>> my_hash('abc') == my_hash('cba') == my_hash('bbb')
# True

# Similarly to the previous hash function, it will have trouble filling up
# the buckets. Even for words of length <= 10, it can only fill 1280 buckets
# (assuming ASCII) and there are MANY more words of length <= 10.

with open('words.txt') as f:
    words = list(f.read().split())

def fill_buckets(newB):
    global B
    B = newB
    buckets = 10000 * [0]
    for w in words:
        buckets[my_hash(w) % 10000] += 1
    return buckets

def buckets_zero(newB):
    return len([x for x in fill_buckets(newB) if x == 0])

def buckets_max(newB):
    return max(x for x in fill_buckets(newB))

def buckets_variance(newB):
    b = fill_buckets(newB)
    avg = sum(b) / len(b)
    return sum(x**2 for x in b) / len(b) - avg**2

# >>> list(map(buckets_zero, [2, 256, 257, 65537, 1000003]))
# [3578, 6277, 1723, 1847, 1772]
# >>> list(map(buckets_max, [2, 256, 257, 65537, 1000003]))
# [20, 365, 9, 10, 9]
# >>> list(map(buckets_variance, [2, 256, 257, 65537, 1000003]))
# [4.96447311, 76.08567311, 1.7798731099999996, 1.9238731099999997, 1.8256731099999994]

# import matplotlib.pyplot as plt
# plt.bar(range(10000), fill_buckets(256))
# plt.show()

## Empty Buckets ##

# Suppose that we insert N values into a hash table with N buckets. What fraction of the buckets do we expect
# will be empty? Assume that N is a large number.

# The chance of a value *not* ending up in a given bucket is 1 - 1/N. The chance of N values all not
# ending up in that bucket is (1 - 1/N)^N. You might know that this number approaches 1/e (where
# e is the base of natural logarithm; 2.718281828) as N grows to infinity. We thus expect the number of
# empty buckets to be N/e on average.

import random

def simulate_hashing(N, factor=100):
    buckets = N * [0]
    for _ in range(factor * N):
        buckets[random.randrange(N)] += 1
    return buckets

def empty_buckets(N):
    buckets = simulate_hashing(N, 1)
    return sum(1 for x in buckets if x == 0)

# >>> empty_buckets(1000000)
# 367587
# >>> 1000000 / math.e
# 367879.44117144233

### Programming 1 Tutorial ###

# ReCodEx: homework solution + new homework


## Bijective Function ##

# Write a function bijective(f, n) that takes a function f whose domain and range are the integers 0 .. n – 1.
# The function should return True if f is bijective, i.e. f is both injective (i.e. f(x) ≠ f(y) whenever x ≠ y)
# and surjective (for every y in the range 0 ≤ y < n, there is some x such that f(x) = y).

def bijective(f, n):
    return set(map(f, range(n))) == set(range(n))

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

### Code quality ###

# Suppose that we have a list of tasks stored in the file tasks.json. You might have
# already seen the JSON format somewhere, but if you haven't, you should get a decent
# idea of how it works from the following example:

# Content of the tasks.json file
#
# [{"name":"prog1 homework","priority":5,"completed":true}
# ,{"name":"exam preparation","priority":1,"completed":false}
# ,{"name":"buy groceries","priority":4,"completed":false}]
#
# As you can see, JSON is almost a valid python code! The json module contains a couple of
# functions that can read this file format and give you the corresponding Python data structure
# (in this case a list of dictionaries).

# Anyways, suppose we want to find all incomplete tasks with priority lower than 5 and print them
# sorted by their priority. Here's one way to do it:

import json
x=open("tasks.json");y=x.read();x.close()
z=json.loads(y)
A=[]
for q in range(len(z)):
    if z[q]["completed"]==False:
        if z[q]["priority"] < 5:
            A.append(z[q])

for i in range(len(A)):
    for j in range(len(A)-1):
        if not(A[j]["priority"]<A[j+1]["priority"]):
            tmp=A[j];A[j]=A[j+1];A[j+1]=tmp

for ix in range(len(A)):
    print("==",A[ix]["name"],A[ix]["priority"],A[ix]["completed"])

# While this works, it has issues:
#
# * You can't tell what the variables are for unless you carefully analyze the code
# * It's not clear what the number 5 is there for unless you already know what problem this
#   code is solving
# * If the input is malformed, the program might do something unexpected or crash without
#   letting the user know what happened
# * The code isn't properly decomposed; if you want to read two JSON files or sort according
#   to a different key, you'll have to rewrite most of the code

# Here's the same program, written in a different way:

import json

# We turn the JSON of the task into an actual python object. We can then access
# the attributes as normal rather than having to do json["priority"] or some such.
class Task:
    def __init__(self, json):
        # We also perform some basic validation to make sure the JSON is alright.
        # In particular, we check that the expected keys are there and the
        # corresponding values also have the expected type.
        #
        # Raising an exception would be better here, but we haven't talked
        # about that yet.
        assert {'name', 'priority', 'completed'} <= set(json.keys()), \
               'JSON items are missing required keys'
        self.name = json['name']
        self.priority = json['priority']
        self.completed = json['completed']
        assert isinstance(self.name, str) and isinstance(self.priority, int) and \
               isinstance(self.completed, bool), 'JSON values have the wrong type'

# A reusable way to load tasks from any file.
def load_tasks(file_path):
    # Using with rather than closing the file manually. If something bad happens
    # after opening the file, with makes sure that it will be closed.
    with open(file_path, "r") as f:
        raw_data = json.load(f)

    return [Task(item) for item in raw_data]

# Global constant instead of a magic value somewhere in the middle of the code.
MAX_PRIORITY = 5

def get_filtered_tasks(tasks):
    # It's easier to tell what the comparison is doing here. Clearly whatever
    # the problem was, there was some limit on the maximum allowable priority.
    filtered = [task for task in tasks if not task.completed and task.priority < MAX_PRIORITY]
    # Don't reinvent the wheel. There's already a perfectly fine sorting algorithm
    # in the standard library, just use it.
    filtered.sort(key=lambda task: task.priority)
    # Also, 'filtered' is much better name than 'A'
    return filtered

# Don't mix output with reading and processing of the data.
def print_tasks(tasks):
    # Give the user some pointers as to what the following lines even mean.
    print('Completed Tasks (sorted by priority):')
    for task in tasks:
        print(f'{task.name} (priority {task.priority})')

def main():
    # All of the previously defined functions allow us to keep main
    # nice and short.
    file_path = "tasks.json"
    tasks = load_tasks(file_path)
    filtered = get_filtered_tasks(tasks)
    print_tasks(filtered)

if __name__ == "__main__":
    main()

# I've added comments to the code explaining the purpose of these changes.
# Now, clearly we had to write more code and presumably spend more time on this,
# so is it really necessary?
#
# In practice, you won't be writing programs that are used just once (e.g. by ReCodEx)
# and the only people who will ever see then are you and me. Most programs have to
# be changed at some point: new features are implemented, requirements change,
# bug are found, etc. When that happens, you want your program to be easy to change.
# Programs written in the first style are usually pretty hard to change.
#
# Similarly, you'll often be writing programs collaboratively. If you're the only person
# who can understand the code you write, this could be a problem. Sometimes, the person
# who needs to understand your code will be future you. I've written some programs that
# I had trouble understanding when I read them again a couple of months later.

# Our colleagues from NSWI170 have a nice set of guidelines for avoiding the worst
# offenders. You can check it here: https://teaching.ms.mff.cuni.cz/nswi170-web/pages/labs/coding/
# but since it's meant for C/C++ I'll just reiterate with Python in mind.

# 1) Decomposition -- you should structure you code into blocks, functions, classes and,
#                     for bigger projects, files and modules. If a bit of code is starting
#                     to get too long, you should think about how to split it into some
#                     components. As a good rule of thumb, if you can no longer give
#                     a nice descriptive name to a component
#                     (e.g. read_input_filter_incomplete_sort_and_print),
#                     it's probably a good time to split it.
#
# 2) Constants -- use constants rather than putting some magic literals in your code,
#                 an example could be the MAX_PRIORITY above. That doesn't mean you shouldn't
#                 ever use literals, but when there's a possiblity that it's not clear what the
#                 literal is there for, you should consider a constant instead.
#
# 3) Do not repeat yourself -- also known as DRY; don't write the same code more than once if
#                              at all possible. In particular, you should resist the urge to
#                              copy&paste code -- generally, that means you should be defining
#                              a function instead.
#
# 4) Global variables -- if you need to use the global keyword, you're probably doing something
#                        wrong. There can be some cases where global is the best way to solve a
#                        problem, but they tend to be very rare. In particular, don't replace
#                        function parameters/results with global variables.
#
# 5) Encapsulation -- if you're using a class, you should stick to using its public interface.
#                     Sometimes, classes will define additional methods or attributes for internal
#                     use (e.g. resize in a dynamic array). You shouldn't be using these from the outside.
#                     For your own classes, it's a good idea to spend some time thinking about
#                     what is the public interface (which methods do you expect users to use) and
#                     what's internal.
#
# This list could go on and on, but let me just mention two additional things:
#
# Good variable names make code much more readable. Unfortunately, what's a good name generally
# depends on the context. There's no best "length" of variables to use. You don't want them to be
# too short but also not too long. Generally, the length should scale with use. If you only use
# a variable in 2-3 lines? Short name can be fine. If you use a variable in your whole program?
# A longer, more descriptive name is appropriate. For example, the following is probably a bad idea:

# Integer square root
def isqrt(number_that_were_computing_the_square_root_of):
    binary_search_beginning_number = 0
    binary_search_ending_number = number_that_were_computing_the_square_root_of
    # etc etc

def main():
    with open('debug_log.txt', 'w') as l:
        # ...
        # 100 lines of code that use the l as a debug log
        #
        pass
    # no reason not to be precise and call it debug_log here or
    # some such

# Comments are also something that programmers struggle with at the beginning. You should
# definitely be commenting your code -- some comments are better than none. But *when* should
# you add a comment?
#
# Generally, if a code is self-explanatory (that is, a normal programmer could easily tell
# what the code is doing just from reading it), comments aren't necessary. For example,
# comments like these are just not helpful:

# Prime factorization from the algorithms lecture
def factors_str(n):
    i = 2 # Initialize i to 2
    s = '' # Initialize s to empty string
    while i * i <= n: # While square of i is less than or equal to n
        if n % i == 0: # If n is divisible by i
            s += str(i) + ' * ' # Add i and the multiplication symbol to the string
            n = n // i # Divide rest by i
        else:
            i += 1 # Otherwise increase i by 1

    s += str(n) # Add the last factor
    return s # Return the final string

# Unless you wrote some exceedingly complicated line of code, you generally shouldn't be
# explaining *what* your code does in the comment. Explaining *why* you're doing something
# is much more helpful. Suppose we are implementing some algorithm and we know the
# result we're looking for can only be at even positions in some list. We have couple of options:

def algo():
    candidates = [] # Imagine some complicated process to fill this list

    # Increase i by 2 in each iteration
    for i in range(0, len(candidates), 2):
        # The above comment is unhelpful; any programmer will be able to tell what's going on
        pass

    # Only check candidates at even positions
    for i in range(0, len(candidates), 2):
        # This is slightly better, but still explains what the code is doing
        pass

    # The above algorithm guarantees that the result will be at
    # an even position; no need to check the odd candidates.
    for i in range(0, len(candidates), 2):
        # Okay, so that's *why* we're only checking half of the list!
        pass

### Writing documentation ###

# As I mentioned earlier, for your semestral project, you'll also need to write
# user and developer documentation. The user documentation is fairly straightforward,
# as you've probably already seen many examples. Simply put yourself into the position
# of a user of your program and think about what sort of information you'd need to
# actually use the program:
#
# * How to run the program?
# * Does the program need any non-standard libraries? (e.g. if the user has to use pip install or some such)
# * What does the program even do? For a game, you could explain the rules of the game
# * What does the input look like? For a game, this could be how to control the game
# * What does the output look like? How to interpret the results?
# * Anything to watch out for? Some special cases that I need to consider?
#
# As for developer documentation, we'll start pretty simple. In the future, you'll be asked to write more
# complex things for your bachelor projects and theses. In Python, a standard way to write developer
# documentation is through something called a *docstring*
#
# A docstring is a special string at the start of a function/class/etc that Python recognizes
# and handles in a special way.

def f():
    '''
    A docstring for the f function.
    '''
    return 0

# Python puts the docstring in a special attribute caled __doc__. For example:
#
# >>> f.__doc__
# '\nA docstring for the f function.\n'
#
# However, a much easier way to access it is with the help function:
#
# >>> help(f)
# Help on function f in module __main__:
#
# f()
#     A docstring for the f function.
#
# If you, as a programmer, want to use a function/class/etc, you typically don't need to know
# exactly how it's implemented. You just need to know what the arguments are, what the output
# is, preconditions or postconditions, etc. This is the sort of stuff you'll find in a docstring
#
# A nice example is the open function:
#
# >>> help(open)
# Help on built-in function open in module _io:
#
# open(
#     file,
#     mode='r',
#     buffering=-1,
#     encoding=None,
#     errors=None,
#     newline=None,
#     closefd=True,
#     opener=None
# )
#     Open file and return a stream.  Raise OSError upon failure.
#
#     file is either a text or byte string giving the name (and the path
#     if the file isn't in the current working directory) of the file to
#     be opened or an integer file descriptor of the file to be
#     wrapped. (If a file descriptor is given, it is closed when the
#     returned I/O object is closed, unless closefd is set to False.)
#
#     ...
#
# It tells you exactly what the arguments are for, what the function does, what
# happens if you try to overwrite a file, etc.
#
# Now, I'm not asking you to write docstrings as detailed as the one for the open
# function, but this should give you an idea of what sort of information one
# expects to find there.
#
# If you want some examples of shorter docstrings, try: help(list.sort), help(str.split),
# help(str.strip) or any other builtin function we've already used before.
