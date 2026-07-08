# Given a natural number n, print all distinct divisors in sorted order.
#
# Examples:
#
# Input : n = 10
# Output: 1 2 5 10
#
# Input:  n = 100
# Output: 1 2 4 5 10 20 25 50 100
#
# Input:  n = 125
#  Output: 1 5 25 125
import math


# basic approch

def getDivisors(n):
    small , large = [],[]
    limit = int(math.sqrt(n))
    for i in range(1,limit+1):
        if n % i == 0:
            if i == n // i:
                small.append(i)
            else:
                small.append(i)  # smaller divisor
                large.append(n // i)  # paired larger divisor

                    # append large divisors in reverse to keep sorted order
    return small + large[::-1]

divisior = getDivisors(100)
print(divisior)


# best approch

def getfector(n):
    res = []

    i = 1

    # forward loop: collect small divisors
    while i * i < n:
        if n % i == 0:
            res.append(i) # smaller divisor
        i += 1

    # handle perfect square case
    if i * i == n:
        res.append(i)
    i -= 1

    # backward loop: collect paired larger divisors
    while i >= 1:
        if n % i == 0:
            res.append(int(n / i)) # paired larger divisor
        i -= 1

    return res


divisor = getfector(-100)

for x in divisor:
        print(x, end=' ')













