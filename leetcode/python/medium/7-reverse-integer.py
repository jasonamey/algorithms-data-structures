# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to
# go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21

class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2 ** 31 - 1 
        INT_MIN = -2 ** 31 
        negative = True if x < 0 else False
        if negative: 
            x *= -1 
        sum = 0 
        while x != 0: 
            digit = x % 10
            sum = (sum * 10) + digit
            x = int(x / 10)
        if sum < INT_MIN or sum > INT_MAX: 
            return 0 
        if negative: 
            sum *= -1 
        return sum 

s = Solution()

assert s.reverse(123) == 321 
assert s.reverse(-123) == -321 
assert s.reverse(120) == 21