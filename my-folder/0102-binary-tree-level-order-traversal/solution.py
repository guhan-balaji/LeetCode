# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        q = deque([root])

        while q:
            level = []
            nodes = []
            for _ in range(len(q)):
                nodes.append(q.popleft())
            
            for node in nodes:
                if not node: continue

                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
            
            if level: levels.append(level)
        
        return levels

