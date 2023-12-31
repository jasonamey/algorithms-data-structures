# Given an array nums of distinct integers, return all the possible 
# permutations. You can return the answer in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

# Example 3:
# Input: nums = [1]
# Output: [[1]]

class Solution:
    # def permute(self, nums):
    #     final = []
    #     if len(nums) == 1: 
    #         return [nums[:]]
    #     for i in range(len(nums)):
    #         n = nums.pop(0)
    #         perms = self.permute(nums)
    #         for perm in perms: 
    #             perm.append(n)
    #         final.extend(perms)
    #         nums.append(n)
    #     return final
    def permute(self, nums):
        def helper(current, left_over, answers):
            if not len(left_over) and current: 
                answers.append(current)
            else: 
                for i in range(0, len(left_over)):
                    new_left_over = left_over[:i] + left_over[i + 1:]
                    new_cur = current + [left_over[i]]
                    helper(new_cur, new_left_over, answers) 
        answers = []
        helper([], nums, answers)
        return answers
    
s = Solution()

ans = [[3, 2, 1], [2, 3, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3], [1, 2, 3]]

assert s.permute([1,2,3]) == ans
assert s.permute([1,2]) == [[2,1], [1,2]]
assert s.permute([1]) == [[1]]