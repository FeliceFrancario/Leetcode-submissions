# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        groupPrev=dummy
        #node1=dummy.next
        #node2=dummy.next
        def reverseListNode(curr,end):
            prev=end
            while curr and curr!=end:
                tmp=curr.next
                curr.next=prev
                prev=curr
                curr=tmp
            return prev
        while True:
            node1=groupPrev
            for i in range(k):
                node1=node1.next
                if not node1:
                    return dummy.next
            groupNext=node1.next
            #groupNext=node1
            curr=groupPrev.next#1 
            newGroupHead=reverseListNode(curr,groupNext)
            #curr ends in the middle or k position
            tmp=groupPrev.next# so save the kth node
            groupPrev.next=newGroupHead# the next of original dummy/previous group so associated to beginning
            groupPrev=tmp#supdate prev to end of previous group( previous kthnode)

        return dummy.next


        
        


        
        

