### Introduction to Algorithms Tutorial ###

# ReCodEx: new homework

## Bases ##

# a) What is 110100_2 in base 10? What is ab_16 in base 10?
# b) What is 95_10 in base 2? In base 16?
# c) What is 67_8 in base 10?
# d) What is 67_10 in base 8?
# e) A byte holds a value from 0_10 to 255_10. In hexadecimal, what is the smallest and largest value that can be stored in a byte?
# f) How many digits does 100_10 have when written in base 5? How many digits does 500_10 have when written in the same base?

# How to extract digits? Let's look at base 10:
#  431 div 10 = 43 (1)
# The remainder gives us the last digit, the quotient is everything BUT the last digit.
# Same thing works for any base.

# a) 1*32+1*16+0*8+1*4+0*2+0*1 = 52; 10*16+11*1 = 171
# b)
#   95 div 2 = 47 (1)
#   47 div 2 = 23 (1)
#   23 div 2 = 11 (1)
#   11 div 2 = 5  (1)
#    5 div 2 = 2  (1)
#    2 div 2 = 1  (0)
#    1 div 2 = 0  (1)
#
# 95_10 = 1011111_2
#
#   95 div 16 = 5 (15)
#    5 div 16 = 0 (5)
#
# 95_10 = 5f_16
# c) 6*8+7*1 = 55
# d)
#   67 div 8 = 8 (3)
#    8 div 8 = 1 (0)
#    1 div 8 = 0 (1)
#
# 67_10 = 103_8
# e) 255 = 256 - 1 = 2^8 - 1 = 16^2 - 1 = 100_16 - 1_16 = ff_16
# f) 100_5 = 5^2 = 25; 100_10 = 400_5 i.e. 3 digits; multiplying by base just adds 0 at the end

## Zeroes versus Ones ##

# Let's say that a number is
#
#   light if its binary representation has more 0s than 1s
#
#   heavy if its binary representation has more 1s than 0s
#
#   balanced if its binary representation has the same number of 0s and 1s
#
# Write a program that reads a decimal integer and reports whether it is light, heavy, or balanced.

n = int(input())
if n == 0: # special case
    print('light')
else:
    ones = 0
    zeros = 0
    while n != 0:
        r = n % 2
        n //= 2
        if r == 1:
            ones += 1
        else:
            zeros += 1
    if zeros > ones:
        print('light')
    elif ones > zeros:
        print('heavy')
    else:
        print('balanced')

## Base 7 to Base 3 ##

# Write a program that reads a number written in base 7, and writes the
# number in base 3.

num = input().strip()
# There are two ways to solve this problem with the tools we have right now:
# we can either use int() to read the number in base10 and then extract the
# digits using arithmetic operations or we can operate on the string directly

n = 0
for digit in num:
    n *= 7
    n += ord(digit) - ord('0')
if n == 0:
    print('0')
else:
    result = ''
    while n != 0:
        result = chr(ord('0') + n % 3) + result
        n //= 3
    print(result)

## Reverse the Digits ##

# Write a program that reads an integer N and prints out N with its digits reversed.
# Do not use any strings (except for reading the input) or lists. You must reverse
# the digits using arithmetic operations only.

# Hint: extract N's digits in order from least significant to most significant;
# use those to build an integer K in which the least significant digit of N
# becomes the most significant digit of K.

n = int(input())
k = 0
while n != 0:
    k *= 10
    k += n % 10
    n //= 10
print(k)

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
