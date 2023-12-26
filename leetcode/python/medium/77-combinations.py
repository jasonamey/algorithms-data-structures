# Given two integers n and k, return all possible combinations of k 
# numbers chosen from the range [1, n].

# You may return the answer in any order

# Example 1:
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] 
# are considered to be the same combination.

class Solution:
    def combine(self, n, k):
        results = []
        def helper(start,comb): 
            if len(comb) == k: 
                results.append(comb[:])
            else: 
                for i in range(start, n + 1):
                    comb.append(i)
                    helper(i + 1, comb)
                    comb.pop()
        helper(1, [])
        return results
    
s = Solution()

assert s.combine(4, 2) ==  [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
assert s.combine(1, 1) == [[1]]