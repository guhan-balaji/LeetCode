# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def max_height(root: Optional[TreeNode], height: int) -> int:
            if not root:
                return height
            
            return max(max_height(root.left, height + 1), max_height(root.right, height + 1))
        
        if not root:
            return True

        l = max_height(root.left, 1)
        r = max_height(root.right, 1)
        diff = abs(l - r)
        
        return diff < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
