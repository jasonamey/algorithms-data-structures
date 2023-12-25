class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    count = 1
    tmp = linkedList
    while tmp.next is not None:
        tmp = tmp.next
        count += 1
    halfWayIdx = count // 2 + 1
    count = 1
    tmp = linkedList
    while count != halfWayIdx:
        tmp = tmp.next
        count += 1 
    return tmp
        
      

