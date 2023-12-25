def insertionSort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(i, len(arr)):
            while(j > 0 and arr[j] < arr[j - 1]):
                swap(j, j-1, arr)
                j -= 1
    return arr
                
def swap(i, j, arr): 
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp