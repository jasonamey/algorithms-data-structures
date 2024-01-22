class Trie: 
    def __init__(self): 
        self.end = False 
        self.children = {}
    
    def insert(self, word):
        trie = self
        for ch in word: 
            if ch not in trie.children: 
                trie.children[ch] = Trie()
            trie = trie.children[ch]
        trie.end = True 
    
    def search(self, word):
        trie = self 
        for ch in word: 
            if not trie or ch not in trie.children: 
                return False 
            else: 
                trie = trie.children[ch]
        return trie.end == True
    
    def startsWith(self, prefix):
        trie = self
        for ch in prefix:
            if ch in trie.children:
                trie = trie.children[ch]
            else:
                return False 
        return True
    
    def commonPrefix(self):
        trie = self 
        prefix = ""
        while (trie and not trie.end and len(trie.children) == 1): 
            for key in trie.children: 
                trie = trie.children[key]
                prefix += key
        return prefix

    def countPrefix(self, word): 
        count = 0 
        trie = self 
        for ch in word: 
            if trie and ch in trie.children: 
                count += 1 
                trie = trie.children[ch]
            else: 
                return count 
        return count

t = Trie()
t.insert("apple")
assert t.search("apple") == True  
assert t.search("app") == False  
assert t.startsWith("app") == True        
t.insert("app")
assert t.search("app") == True 
assert t.commonPrefix() == "app"

t_2 = Trie()
a = ["flower","flow","flight"]
for word in a: 
    t_2.insert(word)
print(t_2.commonPrefix())
