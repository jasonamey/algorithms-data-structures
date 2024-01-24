from collections import defaultdict

class Solution:     
    def groupAnagrams(self, strs) :
        anagrams = defaultdict(list)
        for i in range(len(strs)):
            anagram = self.createAnagram(strs[i])
            anagrams[anagram].append(strs[i]) 
        return list(anagrams.values())
    def createAnagram(self, word): 
        anagram = defaultdict(int)
        for ch in word: 
            anagram[ch] += 1 
        print(str(sorted(anagram.items())))
        return str(sorted(anagram.items()))
   
s = Solution()

assert s.createAnagram("hello") == s.createAnagram("olleh")

strs = ["eat","tea","tan","ate","nat","bat"]

assert str(sorted(s.groupAnagrams(strs))) == str([['bat'], ['eat', 'tea', 'ate'], ['tan', 'nat']])



        