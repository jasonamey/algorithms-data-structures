class Solution:
    def isHappy(self, n):
        s = set()
        while True:
            total = 0 
            while n: 
                total += (n % 10) ** 2
                n //= 10 
            if total == 1: 
                return True 
            else: 
                if total in s: 
                    return False
                else: 
                    s.add(total)
            n = total

s = Solution()
assert s.isHappy(19) == True
assert s.isHappy(2) == False

        