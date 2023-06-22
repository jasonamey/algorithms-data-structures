def binarySearch(array, target):
    lo = 0
    hi = len(array) - 1
    while lo <= hi: 
      mid = lo + (hi - lo) // 2 
      
      test = array[mid]
      if (test == target):
          return mid
      elif(test < target):
          lo = mid + 1
      else: 
          hi = mid - 1
    return -1

a = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]

print(binarySearch(a, 73))