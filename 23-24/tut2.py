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
# 2^82,589,933 − 1
#
# How many digits does this number have, approximately?

# 2^n - 1 has exactly n digits in base 2
# For example, 2^5 - 1 = 31 = 11111_2
#
# Recall that 2^10 ~ 10^3, i.e. 10 digits in base 2 roughly corresponds to 3 digits in base 10.
# 82,589,933 digits in base 2 is therefore around 25,000,000 digits in base 10 (83M / 10 * 3).

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

### Programming 1 Tutorial ###

# ReCodEx: new homework

# In programming, we often want to modify (rather than completely replace) the content of a variable.
# For example, we might wish to increment a variable by 1. Normally, we do this by writing:
#
# x = x + 1
#
# In this week's lecture, you saw that these operations are so common that Python (and many
# other programming languages) have shortcuts for them, such as +=.
#
# x += 1
#
# You also saw the break and continue statements. break is used to exit the loop; continue is used
# to skip the rest of *one* cycle of the loop. break and continue always apply to the nearest loop!
#
# The "random" library has some useful functions that can generate random numbers for us.
# These numbers aren't truly random. Sometimes the term "pseudorandom" is used. If you know
# the state of the random number generator, you can predict all future "random" numbers.
# There are ways to get truly unpredictable random numbers as well, but we won't need these anytime soon.
#
# If we want to make the functions from the "random" library available to us, we need to import it:
#
# import random
#
# Then we can use these functions by prefixing them with "random":
#
# random.randint(1,6)
#
# Finally, in the "sys" library we have some useful input/output functions. Of particular interest is the
# stdin variable which is a special file that represents the standard input. We can iterate over all
# lines of the standard input by doing:
#
# for line in sys.stdin:
#   ...
#
# Note that the variable line *will* contain the newline character at the end. In console, we indicate the
# end of standard input with Ctrl+D (Unix-based systems) or Ctrl+Z and Enter (Windows).

## Rolling N Dice ##

# Read a number N from the console. Simulate rolling N 6-sided dice. Write the value of each die roll, followed by the sum of all of them.
#
# How many dice? 4
# 6 2 6 1
# total: 15
# ===
# How many dice? 2
# 6 2
# total: 8

import random

n = int(input("How many dice? "))
total = 0
rolls = ''
for i in range(n):
    result = random.randint(1, 6)  # Generates an integer from the range 1 to 6 (inclusive).
    rolls += str(result) + ' '
    total += result
print(rolls)
print("total:", total)

## Average ##

# Read a set of floating-point numbers from the console until the user presses ctrl+D (Unix, macOS)
# or ctrl-Z (Windows). Print their average.
#
# 2.5
# 3.5
# 5.5
# 6.5
# ^D
# 4.5

import sys

count = 0
total = 0.0
for line in sys.stdin:
    count += 1
    total += float(line)
# If the user enters no numbers, we would be dividing by zero. So we skip this case.
# Alternatively you could add else branch to tell the user about the problem.
if count != 0:
    print(total / count)

## Second Largest ##

# Write a program that reads a series of non-negative integers from standard input
# until the user presses Ctrl+D or Ctrl+Z. The program should then print the second
# largest of the integers that were read.

import sys

largest  = -1  # Largest number
largest2 = -1  # Second largest number

for line in sys.stdin:
    n = int(line)
    if n >= largest:
        # If we find a new largest number, the original largest
        # number becomes the 2nd largest and the new number becomes
        # the largest. We can do that simulatenously by using multiple assignment.
        largest, largest2 = n, largest
    elif n >= largest2:
        largest2 = n
print("Second largest: ", largest2)

# Think about what happens when the series of input integers contains duplicates.
# We would expect that the 2nd largest number in the series 1 3 3 2 would be 3.
# Try running the code with that series.

## Triangle ##

# Read a number N, then print an N x N triangle of asterisks as in the example below.
#
# Enter N: 6
#      *
#     **
#    ***
#   ****
#  *****
# ******

n = int(input())
for i in range(n):
    symbols = i + 1
    spaces = n - symbols
    print(spaces * ' ' + symbols * '*')

## Double Or Nothing ##

# Read a string and print 'double' if any two adjacent characters are the same, or 'nothing' otherwise.
#
# Enter string: abacuses
# nothing
# ===
# Enter string: lionesses
# double

s = input()
double = False
# Valid indices for a string s are 0, 1, ..., len(s) - 1.
# For example, s[len(s) - 1] == s[-1] is the last character in a string.
# We check the characters at given positions in pairs: 0,1; 1,2; 2,3; etc
# The last pair we need to check is len(s) - 2, len(s) - 1, so we want
# our for loop to end at len(s) - 2, hence the following range(...):
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        double = True
        break  # No need to check the rest, it won't affect the result
if double:
    print('double')
else:
    print('nothing')

## Password Generator ##

# Write a program that generates a random password with 10 lowercase letters.
# The password should contain alternating consonants and vowels.
#
# Sample outputs:
#
#   kimolonapo
#   ritilenora

# For simplicity, we ignore w and y, which can be both vowels and consonants
# in different contexts.
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvxz'

result = ''
for i in range(10):
    if i % 2 == 0: # consonant
        result += random.choice(consonants)
    else: # vowel
        result += random.choice(vowels)
print(result)

# If we didn't know about the choice function, we could do:
# ix = random.randint(0, len(consonants) - 1)
# result += consonants[ix]
#
# How good are these passwords? How long would it take to break if
# we're checking 1 million passwords every second?

## Number Guessing ##

# Generate a random number from 1 to 1000 and have the user guess it by providing too low/too high hints.

import random

n = random.randint(1, 1000)
while True:
    guess = int(input("Your guess? "))
    if guess < n:
        print("Too low!")
    elif guess > n:
        print("Too high!")
    else:
        print("You got it!")
        break

# What's the optimal strategy? How many guesses do we need in the worst case scenario?

## Project Euler 2 ##

# See: https://projecteuler.net/
#
# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

a = 1
b = 2

fibSum = 0

while a < 4_000_000:
    if a % 2 == 0:
        fibSum += a
    # Move a and b one step along the sequence of Fibonacci numbers
    a, b = b, a + b
print(fibSum)
