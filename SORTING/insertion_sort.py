# INSERTION_SORT


# Insertion sort is a simple sorting algorithm that works by iteratively inserting each element of an unsorted list into its correct position in a sorted portion of the list. It is like sorting playing cards in your hands. You split the cards into two groups: the sorted cards and the unsorted cards. Then, you pick a card from the unsorted group and put it in the right place in the sorted group.
#
# Start with the second element as the first element is assumed to be sorted.
# Compare the second element with the first if the second is smaller then swap them.
# Move to the third element, compare it with the first two, and put it in its correct position
# Repeat until the entire array is sorted.

# Time Complexity
#
# Best case: O(n), If the list is already sorted, where n is the number of elements in the list.
# Average case: O(n2), If the list is randomly ordered
# Worst case: O(n2), If the list is in reverse order
def insertionSort(array):
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
            # print("run")
        array[j + 1] = key
        # print("swap")
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

insertionSort(arr)

print("Sorted array: ", end="")
print_array(arr)





