def sortArrayByParity(nums):
    isEven = 0
    isOdd = len(nums) - 1  
    while isEven < isOdd:
        while isEven < isOdd and nums[isEven] % 2 == 0: 
            isEven += 1
        while isEven < isOdd and nums[isOdd] % 2 != 0: 
            isOdd -= 1
        if isEven < isOdd: 
            nums[isEven], nums[isOdd] = nums[isOdd], nums[isEven]
    return nums  

assert sortArrayByParity([3,1,2,4]) == [4,2,1,3]
assert sortArrayByParity([0]) == [0]
assert sortArrayByParity([0,2]) == [0,2]

def sortArrayByParity_logan(nums):
    left = 0
    right = len(nums) - 1 
    while left < right: 
      if nums[left] % 2 == 0: 
        left += 1
      elif nums[right] % 2 != 0: 
        right -= 1
      else: 
        placeholder = nums[left]
        nums[left] = nums[right]
        nums[right] = placeholder
    return nums

assert sortArrayByParity_logan([3,1,2,4]) == [4,2,1,3]
assert sortArrayByParity_logan([0]) == [0]
assert sortArrayByParity_logan([0,2]) == [0,2] 

    