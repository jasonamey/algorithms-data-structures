# Given the head of a singly linked list, reverse the list, 
# and return the reversed list.

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Input: head = [1,2]
# Output: [2,1]

# Input: head = []
# Output: []

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        if not head: 
          return head
        prev = None
        cur = head 
        next = cur.next 
        while cur: 
            cur.next = prev 
            prev = cur
            cur = next 
            if next: 
                next = next.next
        return prev