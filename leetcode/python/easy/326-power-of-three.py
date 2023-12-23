# Given an integer n, return true if it is a power of three. 
# Otherwise, return false.

# An integer n is a power of three, if there exists an integer
# x such that n == 3x.

# Example 1:
# Input: n = 27
# Output: true
# Explanation: 27 = 33

# Example 2:
# Input: n = 0
# Output: false
# Explanation: There is no x where 3x = 0.

# Example 3:
# Input: n = -1
# Output: false
# Explanation: There is no x where 3x = (-1).


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1: 
            return True
        elif n <= 0 or n % 3 != 0: 
            return False
        elif n % 3 != 0: 
            return False
        else: 
            return self.isPowerOfThree( n / 3)
        
s = Solution()

assert s.isPowerOfThree(27) == True 
assert s.isPowerOfThree(0) == False 
assert s.isPowerOfThree(-1) == False
         