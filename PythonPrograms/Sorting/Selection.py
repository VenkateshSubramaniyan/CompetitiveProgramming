def SelectionSort(arr: [int], n:int):
    for i in range(n):
        minptr=i
        for j in range(i+1,n):
            if (arr[j]< arr[minptr]):
                minptr=j
        temp = arr[i]
        arr[i]=arr[minptr]
        arr[minptr]=temp


arr=[13, 46, 24, 52, 20, 9]
SelectionSort(arr, len(arr))
for i in arr:
    print(i,end=" ")

