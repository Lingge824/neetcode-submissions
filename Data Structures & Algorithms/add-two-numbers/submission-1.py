# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1,num2=0,0
        h1=l1
        c1=h1
        count=0
        while c1 is not None:
            num1+=c1.val*10**count
            count+=1
            c1=c1.next

        h2=l2
        c2=h2
        count=0
        while c2 is not None:
            num2+=c2.val*10**count
            count+=1
            c2=c2.next

        summ=num1+num2
        if summ==0:
            return ListNode(0)

        dummy=ListNode()
        cur=dummy
        while summ>0:
            cur.next=ListNode(summ%10)
            summ=summ//10
            cur=cur.next
        
        return dummy.next
    