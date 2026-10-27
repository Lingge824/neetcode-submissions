# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        sechead=slow.next
        prev=None
        slow.next=None
        while sechead:
            temp=sechead.next
            sechead.next=prev
            prev=sechead
            sechead=temp
        firhead=head
        sechead=prev
        while sechead:
            tmp1, tmp2 = firhead.next, sechead.next
            firhead.next = sechead
            sechead.next = tmp1
            firhead, sechead = tmp1, tmp2