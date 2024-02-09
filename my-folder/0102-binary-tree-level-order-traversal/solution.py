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
            res = [[root.val]]
            parents = [root]

        while parents:
            children, children_vals = self.get_immediate_children(parents)
            if children_vals:
                res.append(children_vals)
            parents = children
        
        return res
    
    def get_immediate_children(self, parents: List[Optional[TreeNode]]) -> (List[Optional[TreeNode]], List[Optional[int]]):
        parents = deque(parents)
        children = []
        children_vals= []
        while parents:
            parent = parents.popleft()
            if parent.left:
                children.append(parent.left)
                children_vals.append(parent.left.val)
            if parent.right:
                children.append(parent.right)
                children_vals.append(parent.right.val)
        
        return (children, children_vals)
