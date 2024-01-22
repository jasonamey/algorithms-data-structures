class Trie:
    def __init__(self):
        self.end = False 
        self.children = {}
    
    def insert(self, word: str) -> None:
        trie = self
        for ch in word: 
            if ch not in trie.children: 
                trie.children[ch] = Trie()
            trie = trie.children[ch]
        trie.end = True

    def commonPrefix(self):
        trie = self 
        prefix = ""
        while (trie and not trie.end and len(trie.children) == 1): 
            for key in trie.children: 
                trie = trie.children[key]
                prefix += key
        return prefix         
  
class Solution:
    def longestCommonPrefix(self, strs):
        t = Trie()
        for str in strs: 
            t.insert(str)
        return t.commonPrefix()
