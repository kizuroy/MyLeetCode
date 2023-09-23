def isSubsequence(s: str, t: str) -> bool:
        i = j = 0  # Initialize pointers for s and t

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1  # Move the pointer in s if a match is found
            j += 1  # Always move the pointer in t

        return i == len(s)  # If i reached the end of s, it is a subsequence


aa = "abc"
t = "ahbgdc"

print(isSubsequence(aa, t))