#Given an integer array arr, return the length of a maximum size turbulent subarray of arr.
# A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.
# More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

def maxTurbulenceSize(arr):
    n = len(arr)
    if n <= 2:
        return n if arr[0] != arr[1] else 1
    max_len = 1
    i = 0
    while i < n - 1:
        if arr[i] == arr[i + 1]:
            i += 1
            continue
        j = i
        while j < n - 1 and ((arr[j] < arr[j + 1] and arr[j + 1] > arr[j + 2]) or (arr[j] > arr[j + 1] and arr[j + 1] < arr[j + 2])):
            j += 1
        max_len = max(max_len, j - i + 2)
        i = j
    return max_len

