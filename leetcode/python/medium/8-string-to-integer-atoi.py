class Solution:
    def myAtoi(self, s: str) -> int:
      i = 0 
      while (s[i] == " "): 
        i += 1 
      
      j = len(s) - 1

      while ord(s[j]) < ord('0') or ord(s[j]) > ord('9'): 
        j -= 1

      s = s[i:j+1]

      signed = -1 if s[i] == "-" else 1
      if signed == -1 or s[i] == "+":
        i += 1
      
      cur = 0 
      while i < len(s):
        cur = cur * 10 + int(s[i])
        i += 1 

      cur *= signed

      cur = 2 ** 31 - 1 if cur >= 2 ** 31 -1 else cur 
      cur = -2 ** 31 if cur <= -2 ** 31 else cur 
      
      return cur


s = Solution()

s.myAtoi("   +123")
      

