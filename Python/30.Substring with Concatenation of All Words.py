from collections import Counter

def findSubstring(s, words):
    if not s or not words:
        return []

    len_word = len(words[0])
    total_len = len_word * len(words)
    result = []
    word_count = Counter(words)

    for i in range(len_word):
        left = i
        right = i
        window_count = Counter()

        while right + len_word <= len(s):
            word = s[right:right + len_word]
            right += len_word
            window_count[word] += 1

            while window_count[word] > word_count[word]:
                left_word = s[left:left + len_word]
                left += len_word
                window_count[left_word] -= 1

            if right - left == total_len:
                result.append(left)

    return result

# Example usage:
s = "barfoothefoobarman"
words = ["foo", "bar"]
print(findSubstring(s, words))  # Output: [0, 9]
