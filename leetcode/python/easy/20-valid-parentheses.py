# Given a string s containing just the characters '(', ')', '{', '}', '[' 
# and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.

# Open brackets must be closed in the correct order.

# Every close bracket has a corresponding open bracket 
# of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        open = "([{"
        close = ")]}"
        stack = []
        for ch in s: 
            if ch in open:
                stack.append(ch)
            else:
                if not len(stack):
                    return False
                test = stack.pop()
                print
                if close.find(ch) != open.find(test):
                    return False
        return len(stack) == 0
        
s = Solution()
assert s.isValid("()") == True
assert s.isValid("()[]{}") == True
assert s.isValid("(]") == False