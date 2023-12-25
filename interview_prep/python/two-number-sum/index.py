def twoNumberSum(array, targetSum):
    sums = set()
    for num in array:
      print(num) 
      if num in sums: 
        return [num, targetSum - num]
      else : 
        sums.add(targetSum - num)
    return []
