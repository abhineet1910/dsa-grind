# Print 1 to n using Recursion
#
# Given an integer n. Print numbers from 1 to n using recursion.
#
# Examples:
#
# Input: n = 3
# Output: [1, 2, 3]
# Explanation: We have to print numbers from 1 to 3.
#
# Input: n = 10
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def printNos(n):
    if n == 0:
        # base condition
        return

    if n < 0:
        printNos(n + 1)
        print(n + 1, end=" ")
        return  # <- important!

    # recursive call first
    printNos(n - 1)

    # print after recursion
    print(n, end=' ')

printNos(10)
printNos(-11)
