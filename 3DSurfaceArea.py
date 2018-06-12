def getArea(arr):
    count =0

    for i in range(0,len(arr)):
        for j in range(0,len(arr[i])):
            if arr[i][j] != 0:
                count += 2
            
            if i == 0:
                count += arr[i][j]
            elif arr[i][j] > arr[i-1][j]:
                count += arr[i][j] - arr[i-1][j]
            if i == len(arr)-1:
                count += arr[i][j]
            elif arr[i][j] > arr[i+1][j]:
                count +=  arr[i][j]-arr[i+1][j] 

            if j == 0:
                count += arr[i][j]
            elif arr[i][j] > arr[i][j-1]:
                count += arr[i][j] - arr[i][j-1]
            if j == len(arr[i])-1:
                count += arr[i][j]
            elif arr[i][j] > arr[i][j+1]:
                count += arr[i][j] - arr[i][j+1]

    return count

print(getArea([[1,3,4],[2,2,3],[1,2,4]]))