#“Horizontal Scanning”
def longestCommonPrerfix(strs) -> str:
    if not str: 
        return ""

    shortest = min(strs, key = len)

    for i, char in enumerate(shortest):
        for other in strs:
            if other[i] != char:
                return shortest[:i]
    
    return shortest



print(longestCommonPrerfix(["flower","flow","flight"]))
print(longestCommonPrerfix(["dog","racecar","car"]))

