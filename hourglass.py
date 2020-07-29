import os
rows, cols = (6, 6)
arr = [[0] * cols] * rows

# print(arr)

# step = 0
# for r in range(0, len(arr)):
#     for c in arr[r]:
#         arr[r][step] = 1
#     step += 1
#     print(arr[r])


def hourglassSum(arr):
    hourglasses = []
    for r in range(0, len(arr) - 2):
        for c in range(0, len(arr[r]) - 2):
            hourglasses.append(arr[r][c] + arr[r][c+1] + arr[r][c+2] +
                               arr[r+1][c+1] + arr[r+2][c] + arr[r+2][c+1] + arr[r+2][c+2])
    for i in range(1, len(hourglasses)):
        sort_me = hourglasses[i]
        while hourglasses[i-1] > sort_me and i > 0:
            hourglasses[i], hourglasses[i-1] = hourglasses[i-1], hourglasses[i]
            i = i - 1

    return hourglasses[-1]


if __name__ == '__main__':
    rows, cols = (6, 6)
    arr = [[0] * cols] * rows
    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))
    step = 0
    for r in range(0, len(arr)):
        for c in arr[r]:
            arr[r][step] = 1
        step += 1
    arr = [[-1, 1, -1, 0, 0, 0], [0, -1, 0, 0, 0, 0, ], [-1, -1, -1, 0, 0, 0],
           [0, -9, 2, -4, -4, 0], [-7, 0, 0, -2, 0, 0], [0, 0, -1, -2, -4, 0]]
    result = hourglassSum(arr)

    print(str(result) + '\n')
