# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=node=ListNode()
        #node=node.next
        tens=0
        while l1 and l2:
            if (l1.val+l2.val+tens)<10:
                node.next=ListNode(l1.val+l2.val+tens)
                tens=0
            else:
                node.next=ListNode((l1.val+l2.val+tens)%10)
                tens=1
            l1=l1.next
            l2=l2.next
            node=node.next
        while l1:
            
            if(l1.val+tens)>9:
                node.next=ListNode((l1.val+tens)%10)
                tens=1
            else:
                node.next=ListNode(l1.val+tens)
                tens=0
            l1=l1.next
            node=node.next
        while l2:
            if(l2.val+tens)>9:
                node.next=ListNode((l2.val+tens)%10)
                tens=1
            else:
                node.next=ListNode(l2.val+tens)
                tens=0
            l2=l2.next
            node=node.next
        if tens==1:
            node.next=ListNode(1)

        return dummy.next
        