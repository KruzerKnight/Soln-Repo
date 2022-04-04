# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        s,f=head,head
        for _ in range(k-1):
            f=f.next
        first=f
        while f.next:
            s,f=s.next,f.next
        s.val,first.val=first.val,s.val
        return head