class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    prev = None
    temp = head
    next = None
    while temp is not None:
        next = temp.next
        temp.next = prev
        prev = temp
        temp = next
    return prev


def printLinkedList(head):
    temp = head
    listString = ""
    while temp.next is not None:
        listString += str(temp.value) + " => "
        temp = temp.next
    listString += str(temp.value)
    print(listString)


# l = LinkedList(9)
# l.next = LinkedList(3)
# l.next.next = LinkedList(5)
# l.next.next.next = LinkedList(6)

# printLinkedList(l)
# a = reverseLinkedList(l)
# printLinkedList(a)
