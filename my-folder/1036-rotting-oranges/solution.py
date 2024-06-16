from typing import Tuple, Deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque([])
        fresh_oranges = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                match grid[x][y]:
                    case 1:
                        fresh_oranges += 1
                    case 2:
                        q.append((x, y))
        
        if fresh_oranges == 0:
            return 0
        elif not q:
            return -1
        else:
            minutes = -1
            while q:
                q = self.bfs(q, grid)
                minutes += 1
                fresh_oranges -= len(q)

            return minutes if fresh_oranges == 0 else -1
        


    def bfs(self, q: Deque[Tuple[int, int]], grid: List[List[int]]) -> Deque[Tuple[int, int]]:
        new_rotten = deque([])
        while q:
            r, c = q.popleft()

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = r + dr, c + dc

                if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                    continue
                elif grid[x][y] == 1:
                    grid[x][y] = 2
                    new_rotten.append((x, y))
        
        return new_rotten

