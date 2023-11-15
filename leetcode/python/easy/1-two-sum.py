def twoSum(self, nums, target):
  sums = {}
  for i in range(0, len(nums)):
    if nums[i] in sums  : 
      return [sums[nums[i]], i]
    else : 
      sums[target - nums[i]] = i