#time O(nlogn) | space   O(n) 
def sortedSquaredArray_ONE(array):
    squares = []
    for num in array: 
        squares.append(num ** 2)
    squares.sort()
    return squares

#time O(n) | space O(n)  
def sortedSquaredArray_TWO(array):
    squares = [0 for _ in array]
    smallIdx = 0 
    largeIdx = len(array) - 1
    for idx in reversed((range(len(array)))):
        if (abs(array[smallIdx]) > abs(array[largeIdx])): 
            squares[idx] = array[smallIdx] ** 2
            smallIdx += 1
        else: 
            squares[idx] = array[largeIdx] ** 2
            largeIdx -= 1
    return squares

print(sortedSquaredArray_TWO([-10, -2, 1,2,3,4]))