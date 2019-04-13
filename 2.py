# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        re = r = ListNode(0)
        carry = 0
        num = 0
        while l1 or l2:
            if l1:
                x = l1.val
                l1 = l1.next
            else:
                x = 0
            if l2:
                y = l2.val
                l2 = l2.next
            else:
                y = 0
            num = carry + x + y
            carry = num // 10
            r.next = ListNode(num%10)
            r = r.next
        if carry > 0:
            r.next = ListNode(1)
        return re.next
