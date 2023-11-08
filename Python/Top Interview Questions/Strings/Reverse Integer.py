def reverse(x):
    #If input number is less than 0, sign will be -1 otherwise, sign will be 1.
    sign = [1, -1][x < 0]

    #Reverse the absolute valuse of the input number.
    rev = int(str(abs(x))[::-1])

    # If the reeversed number is greater than 2^31, return 0. 
    # Otherwhise, return the reversed number.
    return sign * rev * (rev < 2**31)