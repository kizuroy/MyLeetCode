def isPalindrome(s: str) -> bool:
    s = ''.join(i for i in s if i.isalnum()).lower()
    return s == s[::-1]

isPalindrome('A man, a plan, a canal: Panama') # True