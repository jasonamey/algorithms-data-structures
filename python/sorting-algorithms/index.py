# 4 5 7 8 2 


# 4 5 7    8 2 


# 4 5   7      8    2   

# 4 5 7   8 2 

def sort(arr):
  for i in range(1, len(arr)):
    idx = i 
    while idx > 0 and arr[idx] < arr[idx - 1]:
      swap(idx, idx - 1, arr)
      idx -= 1
  return arr

def swap(i, j, arr):
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp

def sort_TWO(arr):
  for i in range (0, len(arr) - 0):
    min = arr[i]
    minIdx = i
    for j in range(i + 1, len(arr)):
      if (arr[j] < min): 
        min = arr[j]
        minIdx = j  
    swap(i, minIdx, arr)
  return arr
        

print(sort_TWO([6,5,3,4,62,2]))
