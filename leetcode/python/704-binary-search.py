def search(nums: list[int], target: int) -> int:
    lo = 0 
    hi = len(nums) - 1
    while (lo <= hi):
        mid = (hi + lo)//2
        if nums[mid] == target: 
            return mid
        elif nums[mid] > target: 
            hi = mid - 1
        else: 
            lo = mid + 1
    return -1

#
# class Solution_logan:
#     def search(self, nums: List[int], target: int) -> int:

#         start = 0
#         end = len(nums) - 1

#         while start <= end:
#             mid = (start + end) // 2

#             if nums[mid] == target:
#                 return mid

#             if nums[mid] >= nums[start]:
#                 if nums[start] <= target <= nums[mid]:
#                     end = mid - 1
#                 else:
#                     start = mid + 1
#             else:
#                 if nums[mid] <= target <= nums[end]:
#                     start = mid + 1
#                 else:
#                     end = mid - 1

#         return -1


assert search([-1,0,3,5,9,12], 9) == 4
assert search([-1,0,3,5,9,12], 2) == -1