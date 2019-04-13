# 1.暴力法，最小公倍数
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA
        p2 = headB
        while(p1 != p2):
            p1 = headB if p1 == None else p1.next
            p2 = headA if p2 == None else p2.next
        return p1

 # 2.参照142题 环形链表思路，将一个链表头尾相接就与142题解法一样了（但是此方法改变了链表的原有结构，但是Java解法不会改变，不知道原因）
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB ==None:
            return None
        last = headB
        while last.next:
            last = last.next
        last.next = headB

        cycle = 0
        s = p = p2 = headA
        while p2.next != None and p2.next.next != None:
            p = p.next
            p2 = p2.next.next
            if p == p2:
                cycle = 1
                break

        if cycle:
            while s != p:
                s = s.next
                p = p.next
            return s
        else:
            return None

#Java
class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) {
            return null;
        }
        ListNode last = headB;
        while (last.next != null) {
            last = last.next;
        }
        last.next = headB;

        ListNode fast = headA;
        ListNode slow = headA;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                slow = headA;
                while (slow != fast) {
                    slow = slow.next;
                    fast = fast.next;
                }
                last.next = null;
                return fast;
            }
        }
        last.next = null;
        return null;
    }
}
