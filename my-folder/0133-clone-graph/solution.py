"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        else:
            visited = set()
            clones = dict()
            q = deque([node])

            while q:
                cur = q.popleft()
                if cur.val not in visited:
                    clones[cur.val] = Node(cur.val) if cur.val not in clones else clones[cur.val]
                    
                    for nbr in cur.neighbors:
                        clones[nbr.val] = Node(nbr.val) if nbr.val not in clones else clones[nbr.val]
                        clones[cur.val].neighbors.append(clones[nbr.val])
                        q.append(nbr)

                    visited.add(cur.val)
            
            return clones[1]
            
