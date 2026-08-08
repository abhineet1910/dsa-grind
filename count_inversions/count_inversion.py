def inversionCount(arr):
    # code here
    n = len(arr)
    cnt = 0
    for i in range(n):
        for j in range(i, n):
            if arr[i] > arr[j]:
                cnt += 1
    return cnt

result = inversionCount([5,2,4,6,1,8,2,7,5])
print(result)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2

    left, left_count = merge_sort(arr[:mid])
    right, right_count = merge_sort(arr[mid:])

    merged, merge_count = merge(left, right)

    total_count = left_count + right_count + merge_count

    return merged, total_count

def merge(left, right):
    result = []
    i = 0
    j = 0
    count = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count += len(left) - i

            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1

    return result, count
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

arr, inversion_count = merge_sort(arr)

print("Sorted array: ", end="")
print_array(arr)

print("Inversion Count:", inversion_count)