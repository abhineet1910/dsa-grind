#Quick Sort
# QuickSort is a sorting algorithm based on the Divide and Conquer that picks an element as a pivot and
# partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array
#
# There are mainly three steps in the algorithm:
#
# Choose a Pivot: Select an element from the array as the pivot. The choice of pivot can vary (e.g., first element, last element, random element, or median).
# Partition the Array: Re arrange the array around the pivot.
# After partitioning, all elements smaller than the pivot will be on its left, and all elements greater than the pivot will be on its right.
# Recursively Call: Recursively apply the same process to the two partitioned sub-arrays.
# Base Case: The recursion stops when there is only one element left in the sub-array, as a single element is already sorted.
#



def quicksort(arr,low ,high):

    if (low >= high):
        return
    pivotindex = partition(arr, low, high)
    quicksort(arr, low, pivotindex - 1)
    quicksort(arr, pivotindex + 1, high)
    return arr
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    print("---------------------")
    print("Current Array :", arr)
    print("Pivot =", pivot)
    print("i =",i)
    for j in range(low, high):

        print("Checking", arr[j])
        if arr[j] < pivot:
            i += 1
            print(f"{arr[j]} < {pivot}")
            print("Smaller than pivot")
            print("i becomes", i)
            print(f"Swap index {i} ({arr[i]}) with index {j} ({arr[j]})")
            swap(arr, i, j)
            print("Array :", arr)
        else:

            print(f"{arr[j]} >= {pivot}")

    print("\nFinal Pivot Swap")

    swap(arr, i + 1, high)

    print(arr)

    print("Pivot placed at index", i + 1)


    return i+1
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

arr = quicksort(arr, 0, len(arr)-1)
print("Sorted array: ", end="")
print_array(arr)






