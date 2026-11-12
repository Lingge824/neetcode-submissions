# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced=True
        self.height(root)
        return self.balanced

    def height(self,node):
        if node is None:
            return 0
        leftH=self.height(node.left)
        rightH=self.height(node.right)
        if abs(leftH-rightH)>1:
            self.balanced=False
            return -1
        return 1+max(leftH,rightH)