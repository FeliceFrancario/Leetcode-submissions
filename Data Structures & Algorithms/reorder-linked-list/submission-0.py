# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l=r=head
        while r and r.next:
            l=l.next
            r=r.next.next
        list2=l.next
        l.next=None
        prev=None
        while list2:
            tmp=list2.next
            list2.next=prev
            prev=list2
            list2=tmp
        first, second= head, prev
        while second:
            tmp1=first.next
            tmp2=second.next
            first.next=second
            second.next=tmp1
            first=tmp1
            second=tmp2
        #return head




        

        
        