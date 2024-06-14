from typing import Dict, Set
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_reqs = {i: [] for i in range(numCourses)}

        for [k, v] in prerequisites:
            pre_reqs[k].append(v)
        
        for node in pre_reqs.keys():
            if not self.dfs(pre_reqs, node, set()): return False

        return True

    def dfs(self, pre_reqs: Dict[int, List[int]], cur: int, visited: Set[int]) -> bool:  
        if cur in visited:
            return False
        
        if not pre_reqs[cur]:
            return True

        visited.add(cur)
        for node in pre_reqs[cur]:
            if self.dfs(pre_reqs, node, visited):
                pre_reqs[cur].remove(node)
            else:
                return False
        visited.remove(cur)
        return True

