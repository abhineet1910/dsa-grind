def aggressiveCows(arr, k):
    arr.sort()
    n = len(arr)

    def can_we_place(array, dist, cows):
        cntcows = 1
        last = array[0]
        for i in range(1, len(array)):
            if (array[i] - last) >= dist:
                cntcows += 1
                last = array[i]
        if cntcows >= cows:
            return True
        else:
            return False

    low = 1
    high = arr[-1] - arr[0]
    while low <= high:
        mid = (low + high) // 2
        if can_we_place(arr, mid, k) == True:
            low = mid + 1
        else:
            high = mid - 1
    return high
arr = list(map(int, input().split()))
k = int(input())
print(aggressiveCows(arr, k))