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
        else:
            left_h = self.get_height(root.left, 1)
            right_h = self.get_height(root.right, 1)
        
            if abs(left_h - right_h) > 1:
                return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def get_height(self, node: Optional[TreeNode], height: int) -> int:
        if not node:
            return height
        else:
            return max(self.get_height(node.left, height + 1),
                       self.get_height(node.right, height + 1))
