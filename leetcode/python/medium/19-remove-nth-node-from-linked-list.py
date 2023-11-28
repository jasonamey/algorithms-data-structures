# Given the head of a linked list, remove the nth node 
# from the end of the list and return its head.

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Input: head = [1], n = 1
# Output: []

# Input: head = [1,2], n = 1
# Output: [1]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        nodeCount = 0
        temp = head

        #count number of nodes : 
        while(temp != None):
            nodeCount += 1
            temp = temp.next

        if nodeCount == 0: 
            return None
        
        #see position of node prior to node you're looking to remove : 
        prevNodeNumber = nodeCount - n 

        #if you are looking to remove the head node : 
        if prevNodeNumber == 0: 
            temp = head.next
            head.next = None 
            return temp
        
        curNodeNumber = 1
        cur = head
        while (curNodeNumber != prevNodeNumber):
            cur = cur.next
            curNodeNumber += 1 
        
        temp = cur.next 
        cur.next = temp.next 
        temp.next = None 
        del temp 
        
        return head 
    
#### testing ####

def printLinkedList(head):
    temp = head 
    while temp != None: 
        print(f'{temp.val} -> ', end="")
        temp = temp.next
    print('NONE \n')

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

head = s.removeNthFromEnd(head, 2)
printLinkedList(head) # 1 -> 2 -> 3 -> 4 -> NONE 

            
        
        