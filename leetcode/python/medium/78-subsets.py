# Given an integer array nums of unique elements, 
# return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. 
# Return the solution in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]

class Solution:
    def subsets(self, nums):
      # final = [[]]
      # for num in nums: 
      #     result = []
      #     for perm in final: 
      #         copy = perm[:]
      #         copy.append(num)
      #         result.append(copy)
      #     final.extend(result)
      # return final
      # final = [[]]
      # for num in nums:
      #     final_copy = final[:] 
      #     for ele in final:
      #         final_copy.append([num] + ele)
      #     final = final_copy   
      # return final
      final = [[]]
      for num in nums: 
        for i in range(len(final)):
          curset = final[i]
          final.append(curset[:] + [num])
      return final

s = Solution()

assert s.subsets([1,2,3]) == [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
assert s.subsets([0]) == [[], [0]]
