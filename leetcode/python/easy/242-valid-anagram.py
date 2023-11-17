class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s) != len(t): return False

      sArr = [0 for i in range(26)]
      tArr = [0 for i in range(26)]

      for i in range(len(s)):
        sArr[ord(s[i]) - ord('a')] += 1 
        tArr[ord(t[i]) - ord('a')] += 1 

      for i in range(len(tArr)):
        if sArr[i] != tArr[i]:
          return False
      
      return True

s = Solution()

assert s.isAnagram("anagram","nagaram") == True

assert s.isAnagram("rat","car") == False

assert s.isAnagram("nl","cx") == False
        