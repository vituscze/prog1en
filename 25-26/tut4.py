### Introduction to Algorithms Tutorial ###

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

# How to efficiently search for a value in a list? If we don't know anything
# else about the elements of a list, the best we can do is a sequential search:

def find(a, k):
    for i in range(len(a)):
        if a[i] == k:
            return i
    return -1

# What is the time complexity of this search in the best and worst case?
# For best case we have O(1) since the value we're looking for could be
# the first one; for the worst case we have O(n) since it could also be
# the last one or it could not be present in the list at all.

# The reason why we can't do better than O(n) is that comparing an element of
# the list with the searched value doesn't tell us anything other about the
# other elements, so we have no choice but to try them all. What if we knew
# something else about the list? Sometimes, the list will be *sorted*. Is it
# possible to find a value in a sorted list faster than O(n)?

# Suppose the list is sorted in an increasing order. If we look at the element
# in the middle and find out it's *smaller* than what we're looking for, we
# immediately know that the value can't be in the first half of the list (those
# elements are even smaller). We thus only need to consider the second half.

def bsearch(a, k):
    # The variable lo keeps track of the start of the currently considered range
    # (including the element at position lo). At the start of the search, it's set
    # to zero.
    lo = 0
    # Similarly, the variable hi keeps track of the end of the range. At the start
    # of the search, it's set to len(a) - 1 (the last element in the array).
    hi = len(a) - 1
    # Next up, we keep halving the range until we either find what we're looking
    # for or the range becomes empty. Note that when lo == hi, the range isn't
    # empty yet; it contains just a single element.
    while lo <= hi:
        # Find the middle position of the current range
        mid = (lo + hi) // 2
        if a[mid] == k:
            # We were lucky and the middle element is the one we're looking for
            return mid
        if a[mid] < k:
            # Middle point is too small; what we're looking for can't be in the
            # first half
            lo = mid + 1
        else:
            # Middle point is too large; what we're looking for can't be in the
            # second half
            hi = mid - 1
    # The range is empty and no value was found: it couldn't have been in the list
    return -1

# Does this function always finish? In each step, we decrease the length of the
# range by at least one so it has to eventually either find the element or reach
# an empty range.

# What's the best case time complexity? If the value is in the middle, we find
# it immediately -- O(1). In the worst case, the value isn't present in the list
# and we have to shrink the range to just a single element (after which the loop
# ends). Notice that in each iteration of the loop, we remove half of the range.
# How many times do we have to do that until the range has just a single element?
# O(log n).

# Suppose the list contains multiple elements that have the value k. What happens
# to lo and hi if we remove the first if (i.e. the one with a[mid] == k)?
# Is that useful in any way?

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

n = int(input())
sqrt_n = isqrt(n)
if sqrt_n is None:
    print('Not a square')
else:
    print(sqrt_n)

### Programming 1 Tutorial ###

# Reminder: string splitting and joining, running time of list
# operations, nested lists.
#
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
