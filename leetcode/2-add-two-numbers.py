def addTwoNumbers(self, l1, l2):
    carry = 0
    digits = []
    while l1 is not None and l2 is not None:
        sum_value = l1.value + l2.value + carry
        digits.append(sum_value % 10)
        carry = 1 if sum_value > 9 else 0
        l1 = l1.next
        l2 = l2.next
    node = l1 if l1 is not None else l2
    while node is not None:
        sum_value = node.value + carry
        digits.append(sum_value % 10)
        carry = 1 if sum_value > 9 else 0
        node = node.next
    if carry == 1:
        digits.append(1)
    finalNode = ListNode(digits[0])
    tempNode = finalNode
    for i in range(1, len(digits)):
        tempNode.next = ListNode(digits[i])
        tempNode = tempNode.next
    return finalNode


# def addTwoNumbers_TEST(l1, l2):
#     carry = 0
#     digits = []
#     while l1 and l2:
#         sum_value = l1.pop(0) + l2.pop(0) + carry
#         digits.append(sum_value % 10)
#         carry = 1 if sum_value > 9 else 0
#     node = l1 if l1 else l2
#     while node:
#         sum_value = node.pop() + carry
#         digits.append(sum_value % 10)
#         carry = 1 if sum_value > 9 else 0
#     if carry == 1:
#         digits.append(1)
#     print(digits)
# finalNode = ListNode(digits[-1])
# tempNode = finalNode
# for i in reversed(range(0, len(digits) - 1)):
#     tempNode.next = ListNode(digits[i])
#     tempNode = tempNode.next
# return finalNode


addTwoNumbers_TEST([1, 2, 3], [1, 2, 3, 4])
