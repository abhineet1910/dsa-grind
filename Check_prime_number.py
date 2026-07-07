#Check for Prime Number
#Given a number n, check whether it is a prime number or not.
# Note: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
#
# Input: n = 7
# Output: true
# Explanation: 7 is a prime number because it is greater than 1 and has no divisors other than 1 and itself.
#
# Input: n = 25
# Output: false
# Explanation: 25 is not a prime number because it is divisible by 5 (25 = 5 × 5), so it has divisors other than 1 and itself.
#
# Input: n = 1
# Output: false
# Explanation: 1 has only one divisor (1 itself), which is not sufficient for it to be considered prime.

# BASIC APPROCH

def isPrime(num):
    if num < 2:
        return False
    count = 0
    for i in range (2,num):
        if num % i == 0:
            return False
        else:
            return True

# better approch

def check_Prime(num):

    # Numbers less than or equal to 1 are not prime
    if num <= 1:
        return False

    # Check divisibility from 2 to √n using i*i <= n
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1

    # If no divisors were found, n is prime
    return True

if check_Prime(56):
    print("Prime")
else:
    print("Not Prime")



