### Introduction to Algorithms Tutorial ###

# How to pass the tutorial
#
# * Attendance strongly recommended, but not mandatory
# * Homework
#   - Assigned every week, starting next week
#   - 70% (i.e. 70 points) required to pass the tutorial
#   - Points above 90% go towards the exam (but no more than 10%)
#   - Submitted via ReCodEx (see below), make sure you have an account
#   - Do not copy code from other students or the internet
# * You need to pass the tutorial before you can go to the exam

# Study materials
#
# * GitHub repository
# * Discord server (optional)
# * Recordings
#   - Posted every week to the Discord server
#   - Also available on request

## Powers of two ##

# What is the approximate value of
# a) 2^14
# b) 2^32
# c) 8^8

# We can approximate 2^10 as 10^3. The approximation gets worse the higher the exponent.
# 2^10 = 1,024 ~ 1,000 = 10^3 (2.4% error)
# 2^20 = 1,048,576 ~ 1,000,000 = 10^6 (4.9% error)
#
# Side note: that's why programmers sometimes use special binary prefixes in place of
# SI (metric) prefixes; see https://en.wikipedia.org/wiki/Binary_prefix
#
# 1 kB = 1,000 B
# 1 KiB = 1,024 B
#
# a) 2^14 = 2^4 * 2^10 ~ 16 * 1,000 = 16,000
# b) 2^32 = 2^2 * 2^30 ~ 4 * 1,000,000,000 = 4,000,000,000
# c) 8^8 = (2^3)^8 = 2^(3*8) = 2^24 = 2^4 * 2^20 ~ 16 * 1,000,000 = 16,000,000

## Logarithms ##

# What is the approximate value of
# a) log2(8,000,000,000)
# b) log16(16,000,000)

# Reminder: a^b = c <=> log_a(c) = b (for positive a)
# a) log2(8,000,000,000) ~ log2(2^3 * 2^30) = log2(2^33) = 33
# b) log16(16,000,000) ~ log16(2^4 * 2^20) = log16(2^24) = log16(2^(4*6)) = log16(16^6) = 6

## Slow Connection ##

# A notebook computer's disk holds 500 GB (gigabytes) of data.
# We would like to send the data across an extremely slow network that transfers
# only 1 byte/second. Approximately how long will the transfer take?

# How long are 500 Gs (gigaseconds)?

seconds_in_year = 365 * 24 * 60 * 60

# Roughly 32M seconds in a year. 500,000,000,000 / 32,000,000 ~ 2^39 / 2^25 = 2^14 ~ 16,000 years.
# Actual result is 15844 years, pretty good approximation.

## Squares Mod 4 ##

# Is this statement true or false?
# For all integers n, n^2 mod 4 < 2.
# Prove your answer.

# Reminder: a mod b is the remainder of the (integer) division a div b.
# a = a * (a div b) + (a mod b); 0 <= a mod b < b.

# Let's start by checking if this statement holds for a couple of small numbers.
#   0^2 mod 4 = 0
#   1^2 mod 4 = 1
#   2^2 mod 4 = 0
#   3^2 mod 4 = 1
#   4^2 mod 4 = 0
#   5^2 mod 4 = 1
#   ...
#
# It seems that we get 0 for even numbers and 1 for odd numbers. But this is not a proof!
# We need to show that the result is 0 (1) for ANY even (odd) number.
#
# Even numbers are divisible by 2. We can thus write any even number n as n = 2k (where k is another integer).
# Let's see what happens when we use this identity in the remainder calculation:
#
#   (2k)^2 mod 4 = 4k^2 mod 4 = 0
#
# 4k^2 is ALWAYS a multiple of 4, so there's no remainder.
#
# Similarly, odd numbers can be expressed as 2k + 1:
#
#   (2k+1)^2 mod 4 = 4k^2 + 4k + 1 mod 4 = 4(k^2 + k) + 1 mod 4 = 1
#
# We can immediately see that the number is always 1 higher than a multiple of 4.


### Programming 1 Tutorial ###

# How to pass the tutorial
#
# * Attendance strongly recommended, but not mandatory
# * Homework
#   - Assigned every week, starting next week
#   - 70% (i.e. 70 points) required to pass the tutorial
#   - Points above 90% go towards the test (but no more than 10%)
#   - Submitted via ReCodEx (https://recodex.mff.cuni.cz/)
#     * Check README for useful links (new user guide, student guide)
#   - Do not copy code from other students or the internet
# * Test
#   - Last tutorial, details will be specified later
#   - Additional test dates during the exam period
#   - Everyone has three attempts to pass the test
# * Semestral project
#   - Solve a nontrivial problem in Python
#   - Can be implementation of an algorithm, a simple computer game, etc
#   - Before you start working, submit a proposal via email and wait for confirmation
#     * Description of the problem and specification of the solution
#     * Doesn't have to be long, 1-2 paragraphs is usually enough
#   - To submit a project, you need to provide:
#     * Source code
#     * Test data (sample inputs and outputs, if applicable)
#     * User documentation (explain how to use the program to your users)
#     * Developer documentation (explain how your programs works to other developers)
#   - Deadlines are on the course page (https://ksvi.mff.cuni.cz/~dingle/2024-5/prog_1/programming_1.html)

# Study materials
#
# * GitHub repository
# * Discord server (optional)
# * Recordings
#   - Posted every week to the Discord server
#   - Also available on request

## Python ##
#
# You can download the latest version of python here: https://www.python.org/downloads/
# I'll be using Visual Studio here, which will be using in the summer semester where
# we'll be programming in C#. But feel free to use any IDE you're comfortable with.
#
# Python is an interpreted language. The python executable takes your code and executes
# it. There are also compiled languages (such as C), that first translate the code into
# instructions your CPU can understand. Once compiled, you don't need additional program
# to execute your code, it can be run directly. There are also hybrid languages (that
# use a hybrid approach, like JIT).
#
# The Python interpreter is interactive (also known as REPL). You can write commands and
# the interpreter will interactively evaluate them. This way, we can try parts of our
# program as we write it.
#
# Python has a couple of basic data types. There are two numeric types: int (integers) and
# float (floating point numbers).
#
# >>> type(5)
# >>> type(1.0)
#
# Integers have arbitrary precision. Floats have large, but finite precision. We can express
# numbers in the rough range 1e-324 to 1e308 (both positive and negative) and a couple of
# special values (zero, infinity). Note on notation: 1e308 means 1 * 10^308.
#
# Be careful when using floats, their finite precision can lead to unexpected results:
#
# >>> 0.3 == 3 * 0.1
#
# We also have some arithmetic operations: +, -, *, /, **, //, %
# (addition, subtraction, multiplication, float division, exponentiation, integer division, modulo)
# Note that ^ is NOT exponentiation. It's a bitwise operation that we'll talk about later.
#
# Next data type is boolean. Booleans are logical values. We have constants True and False and operations:
# <, <=, >, >=, ==, !=, and, or, not
# (less than, less than or equal, greater than, greater than or equal, equal, not equal, conjunction, disjunction, negation)
#
# >>> not True
#
# Strings are sequences of characters. They are enclosed in quotation marks (") or apostrophes (').
# If we need to write an apostrophe or a quotation mark inside the string, we can use backslash:
#
# >>> "that's nice"
# >>> "that's \"nice\""
#
# There are other special characters we can express with the backslash, such as newline (\n) or tab (\t).
# If we need to put a backslash into the string, we simply double it:
#
# >>> 'The newline character is \\n'
#
# Strings can be added, multiplied (by a number) and compared.
#
# We'll often need to convert between these data types. For example, if we ask the user to write a number,
# python reads the response as a string and we first need to turn it into a number before we can use arithmetic
# operations on it. For this, we have the following 4 operations: int(...), float(...), str(...), bool(...)
#
# >>> int('5') == 5
# >>> str(True) == 'True'
#
# The programs produces an exception (will be later) if the conversion cannot be done.
#
# >>> int('hello')
#
# For now, we'll be writing console applications. As the name suggests, these applications are meant to
# be used from the console (terminal). Console applications have STANDARD INPUT and STANDARD OUTPUT.
# Unless someone changes these (by redirecting, for example), what the user writes into the console is
# the input and what the program writes into the console is the output. We can read standard input
# using the built-in function input(...) and write into standard output using the built-in function print(...)

name = input("What's your name?\n")
print('Nice to meet you', name)

# If we use input(...) with a string, it first writes the string into stdout before reading a line from stdin.
# Keep that in mind when submitting programs to ReCodEx, which compares the entire stdout (i.e. including the
# lines written by input).
#
# Lastly, Python has branches (if, elif, else) and loops (while, for).

for i in range(10):
    print(i)

for c in name:
    print(c)

## ReCodEx ##

# Homework is automatically graded by ReCodEx. Create an account and join the groups for both
# tutorials by following the new user guide: http://www.ms.mff.cuni.cz/ReCodEx/NewUserDocEng.pdf
# The student guide explains how to use ReCodEx as a student: http://www.ms.mff.cuni.cz/ReCodEx/StudentDocEng.pdf
#
# When you submit a program, ReCodEx will automatically run your code on a set of test cases and
# grades you based on how many test cases successfully passed. A test case can fail for many reasons:
# wrong result, program took too long, program consumed too much memory, program crashed, etc.
#
# If you're not sure why something failed, feel free to write me a DM on Discord or an email.
#
# Sometimes, assignments will have additional requirements that cannot be checked by ReCodEx.
# In these cases, I'll check your solutions and manually adjust the score if the requirements weren't met.
#
# ReCodEx roughly works as follows: each test case has two associated files: test.in and test.out.
# test.in is the file containing the test case input, test.out is the correct output. ReCodEx then runs:
#
# $ python student_code.py < test.in > student.out
#
# And finally, it compares the files test.out and student.out. If they're the same, the test passes.
# In reality, it's a bit more complicated (there are time limits and memory limits to make sure your
# programs can't cause any problems on the ReCodEx servers).

## Paint ##

# Read integers representing the width, length and height of a room in meters,
# and print out the number of square meters of paint required to paint the walls
# and ceiling (but not the floor).

# Width: 5
# Length: 8
# Height: 4
# You need 144 square meters of paint.

w = int(input('Width: '))
l = int(input('Length: '))
h = int(input('Height: '))
ceiling = w * l
walls = 2 * (l + w) * h
print('You need', ceiling + walls, 'square meters of paint.')

## Quotient ##

# Read two integers X and Y, and print their quotient if X
# is exactly divisible by Y, or "indivisible" otherwise.

# Enter X: 8
# Enter Y: 2
# 8 divided by 2 is 4
# ===
# Enter X: 10
# Enter Y: 3
# indivisible

x = int(input('Enter X: '))
y = int(input('Enter Y: '))
if x % y == 0:
    print(x, 'divided by', y, 'is', x // y)
else:
    print('indivisible')

## Largest of Three ##

# Read three integers, and print out the largest of them.

# Enter X: 4
# Enter Y: 17
# Enter Z: 2
# The largest is 17.

x = int(input('Enter X: '))
y = int(input('Enter Y: '))
z = int(input('Enter Z: '))
largest = x
if y > largest:
    largest = y
if z > largest:
    largest = z
print('The largest is', largest)

## Numbers from 2 to 20 ##

# Print the even numbers from 2 to 20 on the console. (Don't use a separate
# print statement for each number!)

n = 2
while n <= 20:
    print(n)
    n = n + 2

## Factorial ##

# Write a program that reads a number N ≥ 0 and prints the value of N!, i.e. 1 ⋅ 2 ⋅ … ⋅ N.

# Enter N: 6
# 6! = 720

n = int(input('Enter N: '))
factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i
print(n, '! =', factorial)
# print(f'{n}! = {factorial}')

## All Divisors ##

# Write a program that reads a positive integer N and
# prints all of its divisors, as well as a count of the divisors.

# Enter N: 12
# 1
# 2
# 3
# 4
# 6
# 12
# There are 6 divisors

n = int(input('Enter N: '))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1
        # count += 1
        print(i)
print('There are', count, 'divisors')

## Making Change ##

# Read a price in Czech crowns. Print out a combination of 20-Kč, 10-Kč, 5-Kč
# and 1-Kč coins that add up to the price, using the smallest possible number
# of coins.

# Enter price: 67
# 20 Kc: 3
# 10 Kc: 0
# 5 Kc: 1
# 1 Kc: 2

price = int(input('Enter price: '))
# c20 = price // 20
# price = price - c20 * 20
#
# If we use the modulo operation, we can avoid creating a variable for
# each coin amount:
print('20 Kc:', price // 20)
price = price % 20
print('10 Kc:', price // 10)
price = price % 10
print('5 Kc:', price // 5)
price = price % 5
print('1 Kc:', price)

## Power of Two ##

# Read an integer. Print "pow" if it is a power of 2, "no" otherwise. (Note: 1
# is actually a power of 2, since 20 = 1).

# Enter number: 64
# pow
# ===
# Enter number: 68
# no
# ===
# Enter number: 256
# pow
# ===
# Enter number: 1
# pow

n = int(input('Enter a number: '))
while n % 2 == 0:
    n = n // 2
if n == 1:
    print('pow')
else:
    print('no')

## Leap Years ##

# Read a year from the console, and write out "leap" if it is a leap year,
# or "no leap" if it isn't.
#
# A year is a leap year if it's divisible by 4, unless it's divisible by 100,
# in which case it isn't a leap year, unless it's divisible by 400, in which case it is actually a leap year.

# Enter year: 1922
# no leap
# ===
# Enter year: 1900
# no leap
# ===
# Enter year: 2000
# leap
# ===
# Enter year: 2020
# leap

year = int(input('Enter year: '))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('leap')
else:
    print('no leap')

