import difflib

def findTheDifference(s: str, t: str) -> str:
    char_count = {}

    # Count character frequencies in s
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Subtract character frequencies in t
    for char in t:
        if char in char_count:
            char_count[char] -= 1
        else:
            # If the character is not in char_count or its count becomes negative, it's the added character
            return char

    # In case there are multiple occurrences of the added character
    for char, count in char_count.items():
        if count != 0:
            return char


def findTheDifferenceXOR(s, t):
    result = 0

    # XOR all characters in s and t
    for char in s:
        result ^= ord(char)

    for char in t:
        result ^= ord(char)

    # Convert the final XOR result back to a character
    return chr(result)


print(findTheDifferenceXOR('abc', 'abce'))
print(findTheDifferenceXOR('a', 'aa'))
