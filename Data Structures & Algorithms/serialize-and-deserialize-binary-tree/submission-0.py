# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        encode=""
        def dfs(node):
            nonlocal encode
            if not node:
                encode+="N,"
                return
            encode+=str(node.val)+","
            dfs(node.left)
            dfs(node.right)

            return
        dfs(root)
        return encode
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals=data.split(',')
        self.i=0
        def dfs():
            if vals[self.i]=='N':
                self.i+=1
                return
            #curr_val=int(curr)
            curr_node=TreeNode(int(vals[self.i]))
            self.i+=1
            curr_node.left=dfs()
            curr_node.right=dfs()
            return curr_node
        
        return dfs()

                



