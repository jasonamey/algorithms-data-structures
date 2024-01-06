# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made 
# by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        
        if not list1 and not list2: 
            return None 
        if not list1: 
            return list2
        if not list2: 
            return list1 
        
        head = None 

        cur1 = list1
        cur2 = list2
        
        tmp = None

        if cur1.val < cur2.val: 
            head = cur1  
            tmp = head 
            cur1 = cur1.next      
        else: 
            head = cur2 
            tmp = head
            cur2 = cur2.next

        while cur1 and cur2:
            if cur1.val < cur2.val: 
                tmp.next = cur1 
                cur1 = cur1.next 
                tmp = tmp.next
            else: 
                tmp.next = cur2
                cur2 = cur2.next
                tmp = tmp.next 
        if cur1: 
            tmp.next = cur1

        if cur2: 
            tmp.next = cur2
        
        return head 

