def reverseString(self, s: list[str]) -> None:
    Len = len(s)
    for i in range(Len//2):
        s[i], s[Len-1-i] = s[Len-1-i], s[i]
    #we can use also
    # return s[::-1]
    

