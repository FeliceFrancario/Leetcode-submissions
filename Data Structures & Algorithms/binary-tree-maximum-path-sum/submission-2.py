# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        

        max_path=float('-inf')
        def dfs(curr ):
            nonlocal max_path
            #if not curr.left and not curr.right:
            #    return curr.val
            if not curr:
                return 0
            left=max(dfs(curr.left),0)
            right=max(dfs(curr.right),0)
            max_path=max(max_path, curr.val+left+right )
            return curr.val+ max(left,right)

        dfs(root)
        return max_path

        