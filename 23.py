#将链表的数值存到列表里排序，再重新构造链表 148题思路一致
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        s = []
        for i in range(len(lists)):
            while lists[i]:
                s.append(lists[i].val)
                lists[i] = lists[i].next
        s.sort()
        re = temp = ListNode(0)
        for i in s:
            temp.next = ListNode(i)
            temp = temp.next
