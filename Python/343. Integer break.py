def maxProductBreak(num):
    if num <= 3:
        return num - 1
    
    product = [0] * (num + 1)
    product[2] = 2
    product[3] = 3

    for i in range(4, num + 1):
        for j in range(2, i // 2 + 1):
            product[i] = max(product[i], product[j] * product[i - j])
    
    return max(product)


# Example usage:
print(maxProductBreak(2))  # Output: 1
print(maxProductBreak(10)) # Output: 36






#Differemt more mathematical aproach
def maxProductBreak2(n):
    if n <= 3:
        return n - 1
    
    quotient, remainder = divmod(n, 3)
    
    if remainder == 0:
        return 3 ** quotient
    elif remainder == 1:
        return 3 ** (quotient - 1) * 4
    else:
        return 3 ** quotient * remainder

# Example usage:
print(maxProductBreak2(2))  # Output: 1
print(maxProductBreak2(10)) # Output: 36