def strStr(haystack: str, needle: str) -> int:
    if not needle or needle == None : return 0

    needle_len = len(needle)

    for i in range(len(haystack) - needle_len + 1):
        if haystack[i: i+needle_len] == needle:
            return i
    return -1



