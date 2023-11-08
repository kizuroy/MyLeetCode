def reverseString(s: list[str]) -> None:
    Len = len(s)
    for i in range(Len//2):
        s[i], s[Len-1-i] = s[Len-1-i], s[i]
    #We can also use -> return s[::-1]
    

