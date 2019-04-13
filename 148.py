#将链表的数值存到列表里排序，再重新构造链表 23题思路一致
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        s = []
        temp = re = ListNode(0)
        while(head):
            s.append(head.val)
            head = head.next
        s.sort()
        for i in range(len(s)):
            temp.next = ListNode(s[i])
            temp = temp.next
        return re.next
