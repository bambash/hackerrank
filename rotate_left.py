def rotLeft(a, d):

    return a[d:]+a[:d]
    # count = 0
    # while count != d:
    #     for index in range(len(a) - 1):
    #         a[index], a[index-1] = a[index-1], a[index]
    #     count += 1
    # return a


print(rotLeft([1, 2, 3, 4, 5], 1))
