# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        elif math.fabs(self.get_height(root.left, 1) - self.get_height(root.right, 1)) < 2:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
    
    
    def get_height(self, root: Optional[TreeNode], height: int) -> int:
        if not root:
            return height
        else:
            return max(self.get_height(root.left, height + 1), self.get_height(root.right, height + 1))
