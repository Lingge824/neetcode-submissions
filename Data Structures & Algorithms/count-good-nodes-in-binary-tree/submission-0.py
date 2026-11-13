# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
    
        def dfs(node,maxvalue):
            if node is None:
                return 0
            res=0
            if node.val>=maxvalue:
                res=1
                maxvalue=node.val
            res+=dfs(node.left,maxvalue)
            res+=dfs(node.right,maxvalue)
            return res
        return dfs(root,root.val)