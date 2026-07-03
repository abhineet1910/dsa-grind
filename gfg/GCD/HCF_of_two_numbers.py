# The Euclidean algorithm is a way to find the greatest common divisor of two positive integers.
# GCD of two numbers is the largest number that divides both of them.
# A simple way to find GCD is to factorize both numbers and multiply common prime factors.
#
# Examples:
#
# input: a = 12, b = 20
# Output: 4
# Explanation:  The Common factors of (12, 20) are 1, 2, and 4 and greatest is 4.
#
# input: a =  18, b = 33
# Output: 3
# Explanation:  The Common factors of (18, 33) are 1 and 3 and greatest is 3.

# solution of the problem
def findGCD(a, b):
    if a == 0:
        return b
    return findGCD(b % a, a)

# Main function
def main():
    a, b = 35, 15
    g = findGCD(a, b)
    print(g)

if __name__ == "__main__":
    main()