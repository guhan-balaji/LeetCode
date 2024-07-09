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
        clones = {}

        def clone(cur: Optional['Node'], clones):
            if not cur: return
            
            if cur.val in clones:
                return clones[cur.val]

            clones[cur.val] = Node(cur.val, [])
            for nbr in cur.neighbors:
                clones[cur.val].neighbors.append(clone(nbr, clones))
            
            return clones[cur.val]

        return clone(node, clones)

