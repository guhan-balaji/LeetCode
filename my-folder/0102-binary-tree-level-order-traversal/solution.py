# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        else:
            
            parents_q = deque([root])
            res = []

            while parents_q:
                res_level = []
                children_q = []

                for parent in parents_q:
                    res_level.append(parent.val)
                    if parent.left:
                        children_q.append(parent.left)
                    if parent.right:
                        children_q.append(parent.right)
                
                res.append(res_level)
                parents_q = children_q

            return res
