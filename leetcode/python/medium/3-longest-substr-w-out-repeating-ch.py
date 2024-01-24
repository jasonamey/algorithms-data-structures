# Given a string s, find the length of the longest substring
#  without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3

# Example 2:
# Input: s = "bbbbb"
# Output: 1

# Example 3:
# Input: s = "pwwkew"
# Output: 3

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      i, j = 0, 0  
      max = 0
      chars = set()
      while j < len(s):
        if s[j] not in chars: 
          chars.add(s[j])
          if len(chars) > max: 
            max = len(chars)
          j += 1 
        else: 
          chars.remove(s[i])
          i += 1 
      return max
    
s = Solution()
            
assert s.lengthOfLongestSubstring("abcabcbb") == 3
assert s.lengthOfLongestSubstring("bbbbb") == 1
assert s.lengthOfLongestSubstring("pwwkew") == 3
assert s.lengthOfLongestSubstring("dvdf") == 3