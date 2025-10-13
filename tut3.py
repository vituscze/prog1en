### Introduction to Algorithms Tutorial ###

# ReCodEx: new homework

# Reminder: a prime number is an integer greater than 1 whose only factors are 1 and itself.
# A simple way to check if a number n is prime is to try all possible factors (from 2 to n - 1).
# We can optimize this by checking only up to sqrt(n), since a composite number must have a factor
# less than or equal to sqrt(n).
#
# Each positive integer has a unique prime factorization. We can find this factorization by a similar process:
# try dividing the number by larger and larger factors until we reduce the number to 1.

## A Large Prime ##

# The largest known prime number is currently
#
# 2^136,279,841 − 1
#
# How many digits does this number have, approximately?

# 2^n - 1 has exactly n digits in base 2
# For example, 2^5 - 1 = 31 = 11111_2
#
# Recall that 2^10 ~ 10^3, i.e. 10 digits in base 2 roughly corresponds to 3 digits in base 10.
# 136,279,841 digits in base 2 is therefore around 42,000,000 digits in base 10 (140M / 10 * 3).

## Bertrand's postulate ##

# Bertrand's postulate, first proven in 1852, states that for every integer n > 1
# there is at least one prime p such that
#
# n < p < 2n
#
# Write a program that reads an integer n > 1 and prints the count of prime numbers p
# in the range n < p < 2n. Also print the percentage of the numbers in this range
# that are prime. For example:
#
# Enter n: 5
# 1 prime number(s) in the range 5 < x < 10
# 25.0 % are prime
#
# Explanation: There are four numbers (6, 7, 8, 9) in that range.
# Only one (7) is prime. 1 / 4 = 25%.

n = int(input("Enter n: "))
total  = 0  # How many numbers are in the range
primes = 0  # How many prime numbers are in the range
for p in range(n + 1, 2 * n):
    isPrime = True
    factor = 2
    # Instead of checking factor <= int(sqrt(p)), which
    # goes through floating point numbers, we check
    # factor * factor <= p which doesn't.
    while factor * factor <= p:
        if p % factor == 0:  # If factor divides p, then we have a composite number
            isPrime = False  # and a composite number can't be a prime
            break  # No need to find other factors
        factor += 1
    # At this point, the isPrime variable contains
    # the correct result and we can use it to increment
    # the primes variable.
    total += 1
    if isPrime:
        primes += 1

print(primes, "prime number(s) in the range ", n, "< n <", 2 * n)
print(100 * primes / total, "% are prime")

# Note that total is actually always n - 1, so we technically don't have
# to keep track of it in the cycle.

## Most Repeated Factor ##

# Write a program that reads an integer n and prints its prime factor that occurs the most times
# in n's prime factorization. (If more than one prime factor has a maximum number of occurrences,
# print the largest such factor.)

n = int(input("Enter n: "))

factor = 2
factorMax = -1  # This keeps track of the most repeated factor
countMax  = -1  # and its exponent

while factor * factor <= n:  # Is this correct? Don't we need to check against the original n?
    count = 0  # This keeps track of the exponent of the prime factor
    while n % factor == 0:
        count += 1
        n //= factor
    if count >= countMax:  # Exponent is higher, we found a factor with even more repetitions
        countMax = count
        factorMax = factor
    # if count > 0:
    #     print(factor, '^', count)
    factor += 1

# Last factor
if n != 1 and 1 >= countMax:
    countMax = 1
    factorMax = n
    # print(factor, '^ 1')

print('Most repeated factor:', factorMax)
print('Repetitions:', countMax)

## Primes with Odd Digits ##

# Write a program to determine how many 3-digit primes exist that have only odd digits.

count = 0
for p in range(100, 1000):
    # p % 2 == 0 checks if the number is even (i.e. last digit is even), we can check
    # the other digits in the same way by first dividing by a power of 10
    if p % 2 == 0 or (p // 10) % 2 == 0 or (p // 100) % 2 == 0:
        continue
    # Same primality check as above
    factor = 2
    isPrime = True
    while factor * factor <= p:
        if p % factor == 0:
            isPrime = False
            break
        factor += 1
    if isPrime:
        # print(p)
        count += 1
print(count)

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

# Closing point about prime numbers: how to find many primes numbers at once efficiently? Prime sieve!

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
for i in range(len(haystack) - len(needle) + 1):
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
for i in range(len(haystack) - len(needle) + 1):
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
    ix = random.randint(0, len(choices) - 1)
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
