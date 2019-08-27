Dictionaer
Second
max
value

d = {'a': 17, 'b': 34, 'c': 18, 'd': 14, 'e': 37, 'e': 8}

values = sorted(d.values(), reverse=True)
print(values)  # [8, 14, 17, 18, 34]
d1 = {}
for val in values:
    for key in d.keys():
        if (d[key] == val):
            d1[key] = val
for index, val in enumerate(d1):
    if (index == 1):
        print("second max value in dict :({}:{})".format(val, d1[val]))

List
second
max
value

l = [1, 3, 4, 3, 6, 3, 8, 2, 9, 11]

firstbig = l[0]
secondbig = l[1]
for i in range(2, len(l)):
    if (firstbig < l[i]):
        secondbig = firstbig
        firstbig = l[i]

print(secondbig)

Without
loops
1
t0
10
print
---------------------------


def tem(i):
    if (i > 10):
        exit(3)

    print(i)
    i += 1
    tem(i)


tem(1)

ex = "aaabhdhjcc"
o / p: "aacc"
---------------------------------

s = "hgfgfdaaaartrrrr"

l = list(s)
a = ""
print(l)
for index, i in enumerate(l):
    k = ''.join(l[index + 1:index + 2])

    if (l[index] == k):
        a += i * 2
        j = l.count(i)
        for n in range(j):
            l.remove(i)

print(a)

Anagram
Cheching
----------------

str1 = input("Enter first anagram :")
str2 = input("Enter first anagram :")

if (len(str1) != len(str2)):
    print("not a anagram")

elif (len(str1) == len(str2)):
    if (sorted(str1) == sorted(str2)):
        print("anagram")

    else:
        print("Noa a anagram")

Duplicates
eliminate in list
----------------------------

l = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

l1 = []
for i in l:
    if i not in l1:
        l1.append(i)

print(l1)

Amstrong
number
---------------

num = input("Enter a number :")
l = list(num)
length = len(l)

tem = int(num)
sum1 = 0
while (tem > 0):
    val = tem % 10
    sum1 += pow(val, length)
    tem = tem // 10

if (sum1 == int(num)):
    print("The number is amstrong number")

else:
    print("Not a amstrong number")

prime
number in range
---------------------

fromnum = int(input("Emter from number :"))
tonum = int(input("Emter to number :"))

for i in range(fromnum, tonum):
    for j in range(2, i - 1):
        if (i % j == 0):
            break
    else:
        print("Prime", i)

febnocii
program
----------------


# Function for nth Fibonacci number

def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


print(Fibonacci(9))

input = 3
4
6
1
o / p = 4
6
6
1
-----------------------------

s = "3461"
s1 = ""
for index, i in enumerate(s):
    if (s[index] < s[index + 1:index + 2]):
        s1 += s[index + 1:index + 2]

    elif (s[index] > s[index + 1:index + 2]):
        s1 += s[index]

print(s1)
----------------------

input = "abcdefgh"

o / p:
a
d
g
b
e
h
c
f
------------------------

s = "abcdefgh"
for i in range(0, len(s) - 1):
    if (s[i] == 'd'):
        break
    print(s[i], end=" ")
    print(s[i + 3:i + 4], end=" ")
    print(s[i + 6:i + 7])

Date
formate:
-------------

s = "20-08-2019"

d = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May',
     '06': 'June', '07': 'July', '08': 'Aug', '09': 'Sep',
     '10': 'Oct', '11': 'Nov', '12': 'Dec'}

key = s[3:5]
if key in d:
    print("{}-{}-{}".format(s[0:2], d[key], s[6:]))

The
goodest
algorithm
for prime number:
    --------------------------------------


def is_prime(n):
    count = 0
    """
    Assumes that n is a positive natural number
    """
    # We know 1 is not a prime number
    if n == 1:
        return False

    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i * i <= n:
        count = count + 1
        # Check if i divides x without leaving a remainder
        if n % i == 0:
            # This means that n has a factor in between 2 and sqrt(n)
            # So it is not a prime number
            return False, count
        i += 1
    # If we did not find any factor in the above loop,
    # then n is a prime number
    return True, count


print(197, ":", is_prime(197))

One
iteration
prime:
-------------------

n = int(input("E:"))
if (n == 2 or n == 3 or n == 5 or n == 7):
    print("true")
else:
    if (n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0):
        print("flase")
    else:
        print("true")

factorial
program
using
dict:
-----------------------------

look_up = {0: 1}


def fact(n):
    if n not in look_up:
        print("recursing when n is {}".format(n))
        look_up[n] = n * fact(n - 1)
    print(look_up)
    return look_up[n]


fact(6)

Polinomial
matrix:
----------------

l = [[1, 2, 3]
    , [4, 5, 6]
    , [7, 8, 9]]
l1 = []
l2 = []
for i in range(len(l)):
    l1.append(l[i][i])

i = 2
for j in range(len(l)):
    l2.append(l[j][i])
    i -= 1

print(sum(l1) - sum(l2))

if in a sting contineously 3 quetion marks appear the return true othrwise false:
    == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==

    s = "9???1???9???1???9"
    a = "?"
    for index, i in enumerate(s):
        if (i is a and s[index + 1] is a and s[index + 2] is a):
            print("True")
            break

    else:
        print("False")


















