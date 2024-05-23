def partition(s):
    result = []

    def backtrack(start, current_partition):
        if start == len(s):
            result.append(current_partition[:])
            return
        for end in range(start + 1, len(s) + 1):
            if s[start:end] == s[start:end][::-1]: #Check for palindrome
                current_partition.append(s[start:end])
                backtrack(end, current_partition)
                current_partition.pop()

    backtrack(0, [])
    return result

s = "aab"
partitions = partition(s)
print(partitions)  # Output: [["a", "a", "b"], ["aa", "b"]]