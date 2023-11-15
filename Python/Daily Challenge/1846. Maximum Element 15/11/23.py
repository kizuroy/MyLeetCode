def maximumElement(arr):
    arr.sort()
    arr[0] = 1

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            arr[i] = arr[i - 1] + 1
    
    return arr[-1]

#Another way we can solve the given problem
def maxElementAfterDecrementingAndRearranging(arr):
    n = len(arr)
    count = [0] * (n + 1)

    for a in arr:
        count[min(a, n)] += 1

    miss = 0
    for i in range(1, n + 1):
        if count[i] == 0:
            miss += 1
        else:
            miss -= min(count[i] - 1, miss)   # erase the 'miss' with the extra frequencies
            
    return n - miss
