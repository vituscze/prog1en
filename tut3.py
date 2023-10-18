### Introduction to Algorithms Tutorial ###

# ReCodEx: new homework

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

## Three ##

# Consider this program:

# n = int(input('Enter n: '))
# 
# b = True
# while n > 1:
#     if n % 3 == 0:
#         n //= 3
#     else:
#         b = False
#         break
#
# print(b)

# a) For which values of n will it print 'True'?
#
# b) What is its best-case and worst-case big-O running time as a function of n?

# The program will print True if n <= 1 (it won't even enter the loop). If it
# does enter the loop, we keep dividing by 3 until we reach 1. If at any point
# the number isn't divisible by 3, we exit the loop and print False. For n > 1,
# True is only printed if n is a power of 3.
#
# Best case scenario is that n <= 1 where we only need O(1) steps. Similary for
# numbers that aren't divisible by 3. Worst case happens when n is a power of 3
# and we need to go through the entire cycle. Since we divide n by 3 in each
# iteration, we need at most log_3(n) iterations to reach 1 - O(log n) steps.

## Largest Prime Gap ##

# A prime gap is the difference between two consecutive prime numbers. For example,
# 7 and 11 are consecutive primes, and the gap between them has size 4.
#
# Write a program that reads an integer N ≥ 3 and prints the largest prime gap among
# primes that are less than N. The program should print the pair of consective primes
# along with the gap size.

import math

n = int(input())
sieve = (n + 1) * [True]
sieve[0] = sieve[1] = False

for i in range(2, math.isqrt(n) + 1):
    if sieve[i]:
        for j in range(i * i, n + 1, i):
            sieve[j] = False

primes = []
for i in range(n + 1):
    if sieve[i]:
        primes.append(i)

gap = 0
start = 0
end = 0
for i in range(len(primes) - 1):
    current = primes[i + 1] - primes[i]
    if current > gap:
        gap = current
        start = primes[i]
        end = primes[i + 1]

print('Largest gap:', gap)
print('Start:', start)
print('End:', end)

## Smallest Multiple ##

# Solve Project Euler's problem 5:
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math

n = 1
for i in range(1, 21):
    # Least common multiple
    n = n * i // math.gcd(n, i)
    # Also available as math.lcm
    # n = math.lcm(n, i)

print(n)

### Programming 1 Tutorial ###

# ReCodEx: new homework

# Strings (and lists) can be sliced. The expression s[i:j] is a substring of
# the string s, starting from the index i (included) up to index j (excluded).
# If the start is left out, Python uses 0. If the end is left out, Python
# uses len(s) (the end of the string). As with the normal indexing operation,
# we can also use negative numbers with the expected meaning.
#
# >>> 'understandable'[5:10]
# 'stand'
#
# There is also a variation of the slicing: s[i:j:k]. It again creates a slice
# from the index i to index j, but this time with a step k. If k is 1, it behaves
# exactly as s[i:j]. Just like with the range(...) function, k can be negative.
#
# >>> 'hello'[::-1]
# 'olleh'
#
# Lists are written as [x1, x2, ..., xn]. n may be zero, in which case we get
# an empty list []. Lists and strings share many similarities. The key differences
# are that a list can contain anything (strings only contain characters):
#
# >>> x = ['hello', 5, True]
#
# The second key difference is that lists are *mutable* - we can change their elements.
#
# >>> x[1] = 'there'
# >>> x
# ['hello', 'there', True]
#
# We can also append new elements to the end of the list using the append method:
#
# >>> x.append(False)
# >>> x
# ['hello', 'there', True, False]
#
# The += operator can be used to add multiple elements at once:
#
# >>> x += ['1', '2']
# >>> x
# ['hello', 'there', True, False, '1', '2']
#
# If we need to add a new element *in the middle* of the list, we can use the insert method:
#
# >>> x.insert(0, 'test')
# >>> x
# ['test', 'hello', 'there', True, False, '1', '2']
#
# And finally, the del operator can be used to delete elements from the list:
#
# >>> del x[0]
# >>> x
# ['hello', 'there', True, False, '1', '2']
#
# Mutability is very convenient, but is one common source of errors. If you have a list
# represented by some variable and you assign that variable to a different variable,
# it does *not* create a copy of the list. The two variables now refer to the same list.
# Modification through one variable will be seen through the other variable.
#
# >>> x = [1,2,3]
# >>> y = x
# >>> x[0] = 5
# >>> y
# [5, 2, 3]
#
# You need to explicitly make a copy by using one of these:
#
# >>> y = x[:]
# >>> y = x.copy()
# >>> y = list(x)

## ASCII or Unicode ##

# Read a string and print either 'ascii' if the string contains only ASCII characters, 'unicode' otherwise.

s = input()
isUnicode = False
for c in s:
    if ord(c) >= 128:
        isUnicode = True
        break
if isUnicode:
    print('unicode')
else:
    print('ascii')

## Contains ##

# Write a function contains that takes two strings S and T, and returns true if S contains T.
# For example, contains('key lime pie', 'lime') should return true. Do not use the in operator.

haystack = input()
needle = input()

found = False
for i in range(len(haystack) - len(needle)):
    matches = True
    for j in range(len(needle)):
        if haystack[i + j] != needle[j]:
            matches = False
            break
    if matches:
        found = True
        break
print(found)

# Less efficient solution with slices

found = False
for i in range(len(haystack) - len(needle)):
    if haystack[i:i + len(needle)] == needle:
        found = True
        break
print(found)

## Lottery Ticket ##

# Write a program that chooses 5 random numbers from the range 1..25, and prints them all.
# No two of the numbers may be the same. The program must choose any possible set of 5 numbers
# with equal probability.

import random

result = []
for i in range(5):
    while True:
        x = random.randint(1, 25)
        if x not in result:
            result.append(x)
            break
print(result)

# Better idea: start with a list of numbers 1..25, pick a random index, add the number to the result
# and remove it from the list

result = []
choices = list(range(1,26))
for i in range(5):
    ix = random.randint(1, len(choices) - 1)
    result.append(choices[ix])
    del choices[ix]
print(result)

# Are there any downsides to this?

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
