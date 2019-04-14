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

 # 2.参照142题 环形链表思路，将一个链表头尾相接就与142题解法一样了
 # （但是此方法改变了链表的原有结构，需要在后面改原来结构）
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
        last.next = headB    #将B链表头尾相接成环

        slow = fast = headA
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  #快慢指针相遇点
                slow = headA  #相遇点到入环点的距离与A头节点到入环点到距离相等
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                last.next = None  #拆掉B链表形成的环，题目要求不能改变链表结构
                return fast
        last.next = None #若AB不相交，也要拆环
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
