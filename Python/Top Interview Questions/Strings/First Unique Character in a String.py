# Given a string s, find the first non-repeating character in it and return its index. 
# If it does not exist, return -1.

def firstUniqChar(self, s: str) -> int:
    # Create a dictionary
    freq = {}

    for i in s:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    
    for i in range(len(s)):
        if freq[s[i]] == 1:
            return i
    return -1

# We can solve it by using collections
import collections

def firstUniqCharCollections(self, s: str) -> int:
    f = collections.Counter(s)
    for i, char in enumerate(s):
        if f[char] == 1:
            return i
    return -1