import json
f = open('283-move-zeroes-data.json')
data = json.load(f)

def moveZeroesChecker(arr: list[int]) -> None: 
  i = 0
  while arr[i] != 0: 
    i += 1
  for j in range(i, len(arr)): 
    if arr[j] != 0: 
      return False
  return True
  
def moveZeroes(arr: list[int]) -> None:
  l = 0
  for i in range(0, len(arr)): 
    if arr[i] != 0: 
      arr[l] = arr[i]
      l += 1     
  for i in range(l, len(arr)):
    arr[i] = 0

a = [0]
moveZeroes(a)
assert a == [0]

a = [1,0]
moveZeroes(a)
assert a == [1,0]


a = [0,1]
moveZeroes(a)
assert a == [1,0]


a = [0,1,0,3,12]
moveZeroes(a)
assert a == [1,3,12,0,0]

a = data
moveZeroes(a)
assert moveZeroesChecker(a)