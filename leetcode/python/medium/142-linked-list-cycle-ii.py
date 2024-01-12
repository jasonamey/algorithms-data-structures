# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        s = set()
        cur = head 
        while cur:
            if cur in s: 
                return cur
            else: 
                s.add(cur)
                cur = cur.next
        return None

            