# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci 
# sequence, such that each number is the sum of the two preceding ones, 
# starting from 0 and 1. That is : 

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.

# Given n, calculate F(n).

class Solution:
    def fib(self, n: int) -> int:
        # if n == 0: 
        #     return 0 
        # if n == 1: 
        #     return 1
        # else: 
        #     return self.fib(n - 1) + self.fib(n - 2)
        # cache = { 0: 0, 1: 1}
        # if n in cache: 
        #     return cache[n]
        
        # else: 
        #     cache[n] = self.fib(n - 1) + self.fib(n - 2)
        
        # return cache[n]
        num_1 = 0
        num_2 = 1 
        for i in range(n):
            num_1, num_2 = num_2, num_2 + num_1
        return num_1
    
s = Solution()

assert s.fib(2) == 1 
assert s.fib(3) == 2
assert s.fib(4) == 3