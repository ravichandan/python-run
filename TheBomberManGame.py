def bomberMan(n, arr):
    if n is 1:
        return arr

    arr2 = []
    for i in range(0, len(arr)):
        arr2.append([])
        for j in range(0, len(arr[i])):
            if arr[i][j] == 'O':
                arr2[i].append(2)
            else:
                arr2[i].append(0)

    print("---- ", arr2)
    for _ in range(0, (n % 4) + 3):
        for i in range(0, len(arr2)):
            for j in range(0, len(arr2[i])):
                if arr2[i][j] == -1:
                    arr2[i][j] = 0
                elif arr2[i][j] == 0:
                    arr2[i][j] = 3
                else:
                    if arr2[i][j] == 1:
                        if i > 0:
                            arr2[i - 1][j] = 0
                        if j > 0:
                            arr2[i][j - 1] = 0

                        if i < (len(arr2) - 1) and arr2[i + 1][j] is not 1:
                            arr2[i + 1][j] = -1
                        if j < len(arr2[i]) - 1 and arr2[i][j + 1] is not 1:
                            arr2[i][j + 1] = -1
                    arr2[i][j] -= 1

    res = list(
        map(lambda x: ''.join(list(map(lambda y: '.' if y is 0 else 'O', x))),
            arr2))
    print("result -- ", res)
    return res


res = bomberMan(
    3, [".......", "...O...", "....O..", ".......", "OO.....", "OO....."])

for i in range(0, len(res)):
    print(res[i])
