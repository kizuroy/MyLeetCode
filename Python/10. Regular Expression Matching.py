'''
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
'''

def isMatch(s, p):
    # Create a DP table with dimensions (len(s) + 1) x (len(p) + 1)
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    
    # Base case: an empty pattern matches an empty string
    dp[0][0] = True
    
    # Handle patterns with '*'
    for i in range(1, len(p) + 1):
        if p[i - 1] == '*':
            dp[0][i] = dp[0][i - 2]
    
    # Fill in the DP table
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
    
    return dp[len(s)][len(p)]

# Example usage:
s1 = "aa"
p1 = "a"
print(isMatch(s1, p1))  # Output: False

s2 = "aa"
p2 = "a*"
print(isMatch(s2, p2))  # Output: True

s3 = "ab"
p3 = ".*"
print(isMatch(s3, p3))  # Output: True