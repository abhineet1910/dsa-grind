# Merge sort is a popular sorting algorithm known for its efficiency and stability.
# It follows the Divide and Conquer approach.
# It works by recursively dividing the input array into two halves,
# recursively sorting the two halves and finally merging them back together to obtain the sorted array.
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1

    return result
def print_array(arr):
    for val in arr:
        print(val, end=" ")
    print()
n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))
print("Original array: ", end="")
print_array(arr)

arr = merge_sort(arr)

print("Sorted array: ", end="")
print_array(arr)


