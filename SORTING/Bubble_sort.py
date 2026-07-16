# Bubble Sort


# bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. This algorithm is not efficient for large data sets as its average and worst-case time complexity are quite high.
#
# Sorts the array using multiple passes. After the first pass, the maximum goes to end (its correct position). Same way, after second pass, the second largest goes to second last position and so on.
# In every pass, process only those that have already not moved to correct position. After k passes, the largest k must have been moved to the last k positions.
# In a pass, we consider remaining elements and compare all adjacent and swap if larger element is before a smaller element. If we keep doing this, we get the largest (among the remaining elements) at its correct position.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped= True
        if (swapped == False):
            break
        print("run")





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

bubble_sort(arr)
print("Sorted array: ", end="")
print_array(arr)



