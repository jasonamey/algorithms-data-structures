class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    nodeToStay = linkedList
    cur = linkedList
    while nodeToStay is not None:
        while cur is not None and cur.value == nodeToStay.value: 
          temp = cur
          cur = cur.next
          temp.next = None
        nodeToStay.next = cur
        nodeToStay = cur    
    return linkedList