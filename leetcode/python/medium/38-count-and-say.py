# The count-and-say sequence is a sequence of digit strings 
# defined by the recursive formula:

# countAndSay(1) = "1"

# countAndSay(n) is the way you would "say" the digit string 
# from countAndSay(n-1), which is then converted into a 
# different digit string.

# To determine how you "say" a digit string, split it into 
# the minimal number of substrings such that each substring 
# contains exactly one unique digit. Then for each substring, 
# say the number of digits, then say the digit. Finally, concatenate
# every said digit.

class Solution:
    def countAndSay(self, n: int) -> str:
        num = "1"
        newNum = ""
        for _ in range(1, n):
          j = 0
          while j < len(num):
            count = 1
            l = j + 1
            while l < len(num) and num[j] == num[l]: 
              count += 1
              l += 1
            newNum = f"{newNum}{count}{num[j]}"        
            j = l
          num = newNum
        return num

s = Solution()

print(s.countAndSay(4))
            
                