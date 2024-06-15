from typing import Set, Tuple
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                islands = islands + 1 if self.explore(x, y, grid, visited) else islands
        return islands

    # returns 1 if it discovers a new island else 0
    def explore(self, x: int, y: int, grid: List[List[str]], visited: Set[Tuple[int, int]]) -> bool:
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            return False
        if grid[x][y] == '0':
            return False
        if (x, y) in visited:
            return False
        else:
            visited.add((x, y))
            self.explore(x - 1, y, grid, visited)
            self.explore(x, y - 1, grid, visited)
            self.explore(x + 1, y, grid, visited)
            self.explore(x, y + 1, grid, visited)
            return True        

