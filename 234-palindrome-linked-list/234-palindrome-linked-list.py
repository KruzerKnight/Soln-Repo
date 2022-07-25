# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast=slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        
        prev=None
        temp=None
        while slow:
            temp=slow.next
            slow.next=prev
            prev=slow
            slow=temp
        
        while prev:
            if prev.val!=head.val:
                return False
            head=head.next
            prev=prev.next
        return True
            