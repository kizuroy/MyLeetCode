def candy(ratings):
    n = len(ratings)
    candies = [1] * n  # Initialize candies array with 1 candy for each child

    # Go from left to right and update candies
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # Go from right to left and update candies, making sure to satisfy the conditions
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    # Sum up the candies array to get the minimum total candies needed
    min_candies = sum(candies)
    return min_candies


print(candy([1,0,2]))