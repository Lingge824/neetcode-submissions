# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tail=head
        length=0
        while tail:
            tail=tail.next
            length+=1
        index=length-n
        cur=head
        prev=None
        while index!=0:
            prev=cur
            cur=cur.next
            index-=1
        if prev:
            prev.next=cur.next
        else:
            head=cur.next
        return head
