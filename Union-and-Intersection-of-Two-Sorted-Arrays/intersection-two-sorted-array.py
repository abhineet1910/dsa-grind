"""
Intersection of Two Sorted Arrays
Intersection of two sorted arrays combines all unique elements that are common to both arrays into a single sorted array.
There are several methods to find the Intersection of two sorted arrays based on whether the input arrays contain duplicate elements or not:
"""
def intersection(arr1, arr2):
    intersection = []

    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            if len(intersection) == 0 or intersection[-1] != arr2[j]:
                intersection.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1

        else:
            j += 1

        # compare here

    return intersection

a = [1,2,1,2,1,2,1,2]
b = [1,1,2,1,2,1,2,1]
a = sorted(a)
b = sorted(b)

print(intersection(a, b))

