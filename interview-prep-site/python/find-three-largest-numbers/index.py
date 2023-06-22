def findThreeLargestNumbers(array):
  arr = [float('-inf'), float('-inf'),float('-inf')]
  for i in array: 
    adjustArr(i, arr)
  return arr

def adjustArr(test, arr):
  idx = 0
  while(idx < len(arr)):
    if test > arr[idx]:
      if idx == 0: 
        arr[idx] = test
      else: 
        arr[idx - 1] = arr[idx]
        arr[idx] = test
    idx += 1



