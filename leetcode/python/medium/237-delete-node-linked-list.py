# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
      temp = node
      prev = None
      while temp.next != None: 
        temp.val = temp.next.val
        prev = temp
        temp = temp.next
      prev.next = None

vals = [1,2,3,4,5]

nodes = [ListNode(i) for i in vals]
nodes = nodes + [None]

head = None

for i,node in enumerate(nodes):
    if i != len(nodes) - 1: 
        node.next = nodes[i + 1] 
    if i == 0: 
        head = node

s = Solution()

s.deleteNode(head.next.next) # from [1,2,3,4,5] to [1,2,4,5]
assert(head.next.next.val) == 4

s.deleteNode(head.next.next) # from [1,2,4,5] to [1,2,5]
assert(head.next.next.val) == 5





 

    
    
  
