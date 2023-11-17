class Solution:
    def firstUniqChar(self, s: str) -> int:
        arr = [ -1 for i in range(26)]
        for i in range(0, len(s)): 
          idx = ord(s[i]) - ord('a') 
          if arr[idx] == -1: 
            arr[idx] = i 
          elif arr[idx] >= 0:
            arr[idx] = -2
        first = 2 ** 63 - 1
        found = False
        for charIdx in arr: 
          if charIdx >= 0: 
            if charIdx < first:
              found = True 
              first = charIdx
        return first if found else -1

s = Solution()
assert s.firstUniqChar("leetcode") == 0 
assert s.firstUniqChar("loveleetcode") == 2
assert s.firstUniqChar("aabb") == -1