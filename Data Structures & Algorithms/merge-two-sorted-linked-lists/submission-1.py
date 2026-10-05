# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=node=ListNode()
        #l1=list1
        #l2=list2
        while list1 and list2:
            if list1.val<list2.val:
                #tmp=l1.next
                node.next=list1
                #l1=tmp
                list1=list1.next
                
            else:
                #tmp=l2.next
                node.next=list2
                #l2=tmp
                list2=list2.next
            node=node.next
        if list1:
            node.next=list1
        if list2:
            node.next=list2
        return dummy.next
            
            