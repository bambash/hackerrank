def maximumToys(prices, k):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for toy in range(0, len(prices) - 1):
            if prices[toy] > prices[toy + 1]:
                prices[toy], prices[toy + 1] = prices[toy+1], prices[toy]
                is_sorted = False

    num_toys = 0
    for toy in prices:
        if k >= 0:
            if k - toy >= 0:
                num_toys += 1
                k -= toy
    return num_toys


print(maximumToys([1, 12, 5, 111, 200, 1000, 10], 50))
