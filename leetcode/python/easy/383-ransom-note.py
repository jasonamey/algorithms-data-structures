from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = defaultdict(int)
        for ch in magazine: 
            d[ch] += 1 
        for ch in ransomNote: 
            if ch not in magazine or d[ch] == 0:
              return False
            else: 
                d[ch] -= 1
        return True 

s = Solution()

assert s.canConstruct("a", "b") == False
assert s.canConstruct("aa", "ab") == False 
assert s.canConstruct("aa", "aab") == True
          

        