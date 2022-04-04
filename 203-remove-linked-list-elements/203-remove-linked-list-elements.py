# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        r=ListNode(next=None)
        r.next=head
        prev=r
        while prev.next!=None:
            if prev.next.val==val:
                prev.next=prev.next.next
            else:
                prev=prev.next
        return r.next