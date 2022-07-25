# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        th=ListNode(next=None)
        head1=th
        l1=list1
        l2=list2
        
        while l1 and l2:
            if l1.val<l2.val:
                th.next=l1
                l1=l1.next
                th=th.next
            else:
                th.next=l2
                l2=l2.next
                th=th.next
        
        if l1:
            th.next=l1
        if l2:
            th.next=l2
        return head1.next