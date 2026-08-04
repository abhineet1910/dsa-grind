def leaders(arr):

    result = []
    n = len(arr)

    maxright = arr[n - 1]
    result.append(maxright)

    for i in range(n - 2, -1, -1):
        if arr[i] >= maxright:
            result.append(arr[i])
            maxright = arr[i]

    reverse(result, 0, len(result) - 1)

    return result


def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

        # for j in range(i +1,n):
        #     if arr[i]<arr[j] :
        #         break
        # else:
        #   result.append(arr[i])
    # return result
arr = [10,12,10,7,1,5,3,2,9]
result = leaders(arr)
print(result)
