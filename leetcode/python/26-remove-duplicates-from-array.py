# O(n) time O(1) space
def removeDuplicates(self, nums: list[int]) -> int:
    isNewIdx = 1
    setIdx = 1
    while isNewIdx < len(nums): 
        if nums[isNewIdx] == nums[isNewIdx - 1]: 
            isNewIdx += 1
        else: 
            nums[setIdx] = nums[isNewIdx]
            isNewIdx += 1
            setIdx += 1
    return setIdx

