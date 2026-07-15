# SELECTION SORT

# Selection Sort is a comparison-based sorting algorithm. It sorts by repeatedly selecting the smallest (or largest) element from the unsorted portion and swapping it with the first unsorted element.
#
# Find the smallest element and swap it with the first element. This way we get the smallest element at its correct position.
# Then find the smallest among remaining elements (or second smallest) and swap it with the second element.
# We keep doing this until we get all elements moved to correct position.


def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):

        # Assume the current position holds
        # the minimum element
        min_idx = i

        # Iterate through the unsorted portion
        # to find the actual minimum
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                # Update min_idx if a smaller element is found
                min_idx = j

        # Move minimum element to its
        # correct position
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


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

selection_sort(arr)

print("Sorted array: ", end="")
print_array(arr)


