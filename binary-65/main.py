arr =[1, 2, 6, 0, 3, 5, 4, 8, 7, 12, 9, 10, 13, 17, 11, 18, 14, 19, 16, 15]

for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            print(j)
