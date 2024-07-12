class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q: Deque[Tuple[int, int]] = deque([])
        fresh_oranges = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
   
        if fresh_oranges == 0 : return 0
        if not q : return -1

        minutes = 0
        while q and fresh_oranges > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    x, y = r + dr, c + dc
                    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) : continue
                    if grid[x][y] == 1:
                        grid[x][y] = 2
                        q.append((x, y))
                        fresh_oranges -= 1          
            minutes += 1

        return minutes if fresh_oranges == 0 else -1        

