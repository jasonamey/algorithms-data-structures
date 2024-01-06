class Solution:
    def letterCombinations(self, digits):
        def helper(cur, left_over):
            if not left_over:
                ans.append(cur[:])
            else: 
                for ch in nums_to_letters[left_over[0]]:
                    helper(cur + ch, left_over[1:])
        ans = []
        
        nums_to_letters = {
            '2' : 'abc', 
            '3' : 'def', 
            '4' : 'ghi', 
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        if digits: 
            helper("",digits)
        return ans
    
s = Solution()

assert s.letterCombinations("23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"]
assert s.letterCombinations("") == []
assert s.letterCombinations("2") == ["a","b","c"]
            