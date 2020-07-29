def bubbleSort(a):
    length = len(a)
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(0, length -1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                is_sorted = False
    return(a)       
print(bubbleSort([3,7,4,6,7,9,4,3134,7,9,65,4,3,56,8,6543,6,789,8,76,3,35,7,89]))

def quickSort(a):
    length = len(a)
    if length <= 1:
        return a
    else:
        pivot = a.pop()
    higher = []
    lower = []
    for i in a:
        if i > pivot:
            higher.append(i)
        else:
            lower.append(i)
    return quickSort(lower) + [pivot] + quickSort(higher)
print(quickSort([39,4,523,7,324,524,6457,468,468,34,5235,346,58,345,246,468,568,9]))


def insertionSort(a):
    length = len(a)
    for i in range(1, length):
        while a[i] < a[i-1] and i > 0:
            a[i], a[i-1] = a[i-1], a[i]
            i -= 1
    return a
print(insertionSort([8,6,5,4,3,5,7,8,9,8,7,6,4,3,23,45,67,8,7,654,123,2,234,56,8,9,90,987,6]))