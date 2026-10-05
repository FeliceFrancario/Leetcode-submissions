"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        cur=head
        #head_list=[]
        mapping={}
        while cur:
            #head_list.append([cur.val,cur.next,cur.random])
            #head_list.append(Node(cur.val))
            mapping[cur]=Node(cur.val)
            cur=cur.next
            

            #copy.next=Node(cur.val)
        l=head
        while l:
            mapping[l].next=mapping.get(l.next)
            mapping[l].random=mapping.get(l.random)
            l=l.next

        return mapping[head]
        