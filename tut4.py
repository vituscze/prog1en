### Introduction to Algorithms Tutorial ###

# ReCodEx: new homework

# Attendance bonus points

## Simplifying a Fraction ##

# Write a program that reads integers a and b, and prints the fraction a / b in unsimplified and simplified form.
# To simplify the fraction, divide by the greatest common divisor of a and b. For example:
#
# Enter a: 12
# Enter b: 20
# 12 / 20 = 3 / 5

# Reminder: a greatest common divisor of a and b is the largest integer that divides both a and b. We
# use Euclid's algorithm to find it. It is based on the fact that gcd(a, b) = gcd(b, a % b).

a = int(input("Enter a: "))
b = int(input("Enter b: "))

# Euclid's algorithm
x = a
y = b
while y > 0:
    x, y = y, x % y

# x is now the gcd of a and b. We know it divides both numbers (otherwise it wouldn't be gcd)
# so we can use integer division (//) to simplify the fraction.
print(a, '/', b, '=', a // x, '/', b // x)

# How to tell if one algorithm is better than other? We express the number
# of steps taken by the program (and by step we mean some basic operation
# of the program, such as arithmetic operation, variable assignment, etc)
# as a function of the size of the input.
#
# However, for most programs these functions are going to be very messy
# and thus hard to compare. Instead, we approximate them by finding a
# nice approximation that serves at the upper bound (ideally smallest
# possible). We also typically only care about the asymptotic growth
# (how does the function behave as the size of the input goes to
# infinity) and for that we use the big-O notation.
#
# We say f(n) = O(g(n)) (sometimes we use set membership instead of the
# equal sign) when f(n)/g(n) approaches some finite number as n increases.
#
# For example, 2n = O(n), because 2n/n approaches 2. Similarly,
# n = O(n^2) because n/n^2 approaches 0. However, n != O(log n) because
# n/log n goes to infinity.

## Powers and Logs ##

# a) Is 2^(n+1) = O(2^n)?
#
# b) Is 2^(2n) = O(2^n)?
#
# c) Is log_2(n) = O(log_4(n))?

# Let's take a look at f(n)/g(n) and see what happens as we increase n.
# In a) we have 2^(n+1)/2^n, which can be simplified to just 2. f(n)/g(n)
# is thus always 2 no matter the value of n. And so 2^(n+1) = O(2^n).
#
# In b) we have 2^(2n)/2^n, which is 2^n. As n goes to infinity, so does
# 2^n. Thus 2^(2n) != O(2^n).
#
# In c) we have log_2(n)/log_4(n). Recall that log_4(n) = log_2(n)/2. We
# can simplify to 1/2 and thus log_2(n) = O(log_4(n)).

## Growth Rates ##

# Order these functions by increasing growth rate: n!, 2^n, n^10, n^log(n), 10^n, n^2.
#
# Let's start by writing down the trivial comparisons:
#
# 1) n^2 < n^10 < n^log(n)
# 2) 2^n < 10^n
#
# What's larger? n^log(n) or 2^n?
#
# n^log(n) = (2^log_2(n))^log(n) = 2^(log_2(n) * log(n)) which clearly grows slower than 2^n.
#
# We therefore have n^2 < n^10 < n^log(n) < 2^n < 10^n.
#
# Finally, what about n!? Let's consider n!/10^n:
#
#  1 *  2 *  3 *  4 * ... * 20 * 21 * ...    1    2         20
# --------------------------------------- = -- * -- * ... * -- * ...
# 10 * 10 * 10 * 10 * ... * 10 * 10 * ...   10   10         10
#
# The first 9 terms will give us a really small number, but after that
# we're multiplying by numbers >1. For large enough n, this will easily
# outdo the first 9 terms and give us arbitrarily large result.
#
# n^2 < n^10 < n^log(n) < 2^n < 10^n < n!

## Integer Square Root ##

# Write a program that reads an integer n ≥ 0 and prints the square root of n
# (if it is an integer), or otherwise 'Not a square'. Do not use any
# floating-point numbers. Your program should run in O(log n).

def isqrt(n):
    # Suppose we had an array of squares a = [0, 1, 4, 9, 16, 25, ..., n * n].
    # The defining property of this array is that a[i] == i * i. If we wanted
    # to find the square root of any number, we just need to find the correct
    # index, which we can do with binary search. The question is: can we do this
    # without creating the entire array (which would take too long)?
    lo = 0
    hi = n
    while lo <= hi: # At least one number in the range
        mid = (lo + hi) // 2
        if mid * mid == n: # a[mid] == mid * mid
            return mid
        if mid * mid < n:
            lo = mid + 1
        else:
            hi = mid - 1
    return None

### Programming 1 Tutorial ###

# ReCodEx: new homework

## Letter Histogram ##

# Write a program that reads a series of input lines and determines how many times each letter
# A-Z appears in the input. You should ignore case, considering 'a' and 'A' to be the same letter.
# Ignore any characters that are not letters from the Latin alphabet. The input text is guaranteed
# to contain at least one letter.
#
# The program should print the most frequent letter with a count of its occurrences. It should
# also print a histogram showing each letter's frequency as a fraction of all input letters,
# rounded up to the nearest percent. For example, if 3.7% of letters are N, the program should
# print 'n: ****'.
#
# Sample input:
#
# The quick fox jumped over the lazy dog.
# Then the dog got up and jumped over the fox.
#
# Sample output:
#
# Most frequent letter: e (9)
#
# a: *
# b:
# c: *
# d: **
# e: ***
# f: *
# g: *
# h: **

import sys

# A counter for each letter of the English alphabet.
counts = [0] * 26
# Total amount of letters in the text.
total = 0
for line in sys.stdin:
    for c in line:
        c = c.lower()
        # Ignore characters that aren't letters.
        if 'a' <= c <= 'z':
            total += 1
            ix = ord(c) - ord('a')
            counts[ix] += 1

freqMax = 0
freqLetter = ''
# We need to find the highest number in the list counts (i.e. the highest
# frequency) and the corresponding letter (which is given by the index).
#
# Notice we can't just do
#
# for i in counts:
#     ...
#
# because we also need to know the index to figure out which letter the
# count corresponds to.
for i in range(len(counts)):
    if counts[i] > freqMax:
        freqMax = counts[i]
        freqLetter = chr(ord('a') + i)
print('Most frequent letter: ' + str(freqLetter) + ' (' + str(freqMax) + ')')

for i in range(len(counts)):
    letter = chr(ord('a') + i)
    stars = round(counts[i] / total * 100)
    print(str(letter) + ': ' + (stars * '*'))

# One thing to watch out for is list multiplication when creating
# lists of lists. If you do:
#
# >>> x = 3 * [3 * [0]]
# >>> x
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#
# It really seems like we got a 3 by 3 matrix. But the three rows
# of the matrix are shared!
#
# >>> x[0][0] = 1
# >>> x
# [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
#
# One way to solve this is for example:
#
# >>> x = [3 * [0] for _ in range(3)]
#
# We'll talk about this syntax later.
#
# Tuples are basically immutable lists. Immutability is sometimes useful
# (if we know we won't need the mutability, it can prevent silly bugs).
#
# In bigger programs, we often need to perform the same task multiple times.
# For example, we might want to sort two or more lists. While writing the
# sorting algorithm multiple times works, it's far from ideal. Apart from
# having to write the code multiple times, it will also create problems if we
# need to change the code (we found a bug, for example). We'd have to go through
# the entire program and fix each bit of code separately.
#
# In Python, we can solve this by defining functions. Once we have a function,
# we can simply call it multiple times. Functions can have parameters (essentially
# the input of the function), such as a list to be sorted or a number for primality
# checking. Functions can also produce some output. Inside the function, we can use
# a special return statement to specify what the output of the function is. Note
# that return exits the function, no other code after return is executed.
#
# When we assign to a variable inside a function, Python will create a new
# local variable, different from all the variables outside of the function (even
# if they have the same name). In general, it's good practice to only use local
# variables and parameters.

## Local and Global ##

# What will this program print?

a = 2
b = 3

def foo():
  a = b + 1
  a = a + 1
  return a

def bar():
  global b
  b = a + 3
  return b

def baz():
  return a + b

def thud():
  a = b + 1
  b = a + 1
  return a

print(foo())
print(bar())
print(baz())
print(thud())

# foo() returns 5, doesn't change the global a or b
# bar() returns 5, changes the global b to 5
# baz() returns 7, because b is now 5
# thud() is an error because b is a local variable and we're trying to use it
#   before it's initialized

## Lots of References ##

# Recall that a[:] makes a copy of the list a. It's the same as a[0:len(a)], or as a.copy().
#
# What will this program print? Why?

def bar(a):
    for i in range(len(a)):
        a[i] += 1
        a = a[:]

def foo(a):
    for b in a + a[:]:
        bar(b)
        bar(b[:])

m = [[1, 2], [3, 4]]
foo(m)

# Because bar replaces a with a copy after the first iteration of the loop,
# it only adds 1 to the first element of the list.
#
# Inside foo, the variable b goes over a[0], a[1], a[0] and a[1]. Notice that
# when going over a[:], we still access a[0] and a[1] -- this is because a[:]
# makes a SHALLOW copy. The first call of bar increments the first element of
# the list, as we established. The second call doesn't do anything interesting
# because the increment happens on a copy.
#
# The final result is thus [[3,2],[5,4]].

## Matrix Sum ##

# Write a function that takes two matrices, and returns the sum of the matrices.
# Assume that the matrices have the same dimensions.

def add_matrix(a, b):
    # We need to create a new matrix with same dimensions as a and b, but
    # notice we cannot just do a.copy() because the copy is *shallow*.
    c = [len(a[0]) * [0] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[i])):
            c[i][j] = a[i][j] + b[i][j]
    return c

## Matrix Product ##

# Write a function that takes two matrices, and returns the product of the matrices.
# Assume that the matrices have dimensions that are compatible for multiplication.

def mul_matrix(a, b):
    rows_a = len(a)
    shared = len(b)  # We can assume the sizes are compatible
    cols_b = len(b[0])

    # Final matrix has dimensions rows_a x cols_b
    c = [cols_b * [0] for _ in range(rows_a)]
    for i in range(len(c)):
        for j in range(len(c[i])):
            for k in range(shared):
                c[i][j] += a[i][k] * b[k][j]
    return c

# What's the time complexity?

## Largest product in a series ##

# Solve Project Euler's problem 8:

# Find the thirteen adjacent digits in the 1000-digit number that have the
# greatest product. What is the value of this product?

number = '''
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
'''

digits = []
for d in number:
    if '0' <= d <= '9':
        digits.append(int(d))

# We could try all starting positions for the 13 digits and compute the
# product for each. This would definitely work, but wouldn't be feasible for
# larger number of digits. Can we do it better? If the number had no zeros,
# we could keep track of the product of the last 13 digits and when moving one
# digit forward, divide by the last digit and multiply by the new digit.
# To handle zeros, we just need to remember how many of them are in the last 13
# digits!

product = 1
product_len = 0
zeros = 0
highest = 0

for i in range(len(digits)):
    # Add a digit
    product_len += 1
    if digits[i] == 0:
        zeros += 1
    else:
        product *= digits[i]
    # (Possibly) remove a digit
    if product_len > 13:
        product_len -= 1
        if digits[i - 13] == 0:
            zeros -= 1
        else:
            product //= digits[i - 13]
    # If we have 13 digits in our product and none of them are zeros...
    if product_len == 13 and zeros == 0 and product > highest:
        highest = product

print(highest)
