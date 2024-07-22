def insertionSort(inputArr):
    arr=inputArr.copy()
    n=len(arr)
    for i in range(1,n):
        currentptr=i
        swapper=i
        while arr[swapper]>=arr[currentptr] and swapper>-1:
            temp=arr[swapper]
            arr[swapper]=arr[swapper-1]
            arr[swapper-1]=temp
            swapper-=1

    for i in arr:
        print(i,end=" ")

if __name__ == "__main__":
    arr=[5,4,57,2,65,93,56]
    insertionSort(arr)

