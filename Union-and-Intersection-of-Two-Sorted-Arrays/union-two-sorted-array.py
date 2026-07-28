def union_arr(arr1, arr2):

    union = []

    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):

        if arr1[i] < arr2[j]:

            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])

            i += 1

        elif arr1[i] > arr2[j]:

            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])

            j += 1

        else:

            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])

            i += 1
            j += 1

    while i < len(arr1):

        if len(union) == 0 or union[-1] != arr1[i]:
            union.append(arr1[i])

        i += 1

    while j < len(arr2):

        if len(union) == 0 or union[-1] != arr2[j]:
            union.append(arr2[j])

        j += 1

    return union


a = [4, 5, 6, 7]
b = [1, 5, 6, 8]

print(union_arr(a, b))