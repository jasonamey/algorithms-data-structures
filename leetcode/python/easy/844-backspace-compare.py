# Given two strings s and t, return true if they are equal when both 
# are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

# Example 1:
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac"

# Example 2:
# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become ""

# Example 3:
# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b"

#time O(n + m) space(n + m)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.removeBackspace(s) == self.removeBackspace(t)    
    def removeBackspace(self, s): 
        chars = []
        for char in s: 
            if char != "#":
                chars.append(char)
            else: 
                if chars: 
                    chars.pop()
        return "".join(chars)
            
s = Solution()

assert s.backspaceCompare("ab#c","ad#c") == True
assert s.backspaceCompare("ab##","c#d#") == True
assert s.backspaceCompare("a#c","b") == False