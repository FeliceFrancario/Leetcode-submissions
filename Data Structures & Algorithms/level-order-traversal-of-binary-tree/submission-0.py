# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res=[]
        def bfs(node):
            queue=deque([node])
            #if not node:
            #    return None

            while queue:
                qlen=len(queue)
                level=[]
                for i in range(qlen):
                    curr=queue.popleft()
                    if curr:
                        queue.append(curr.left)
                        queue.append(curr.right)
                        level.append(curr.val)
                if level:
                    res.append(level)
        bfs(root)
        return res    


        