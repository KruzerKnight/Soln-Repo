# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def length(th):
            count=0
            while(th!=None):
                count+=1
                th=th.next
            return count
        l1=length(headA)
        l2=length(headB)
        while l1>l2:
            headA=headA.next
            l1-=1
        while l2>l1:
            headB=headB.next
            l2-=1
        while(headA!=headB):
            headA=headA.next
            headB=headB.next
        return headA