class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque([])

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    q.append([r, c])
                else:
                    mat[r][c] = -1
        

        while q:
            [r, c] = q.popleft()

            for [dr, dc] in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                x, y = r + dr, c + dc

                if x < 0 or y < 0 or x >= len(mat) or y >= len(mat[0]) or mat[x][y] != -1:
                    continue
                
                mat[x][y] = mat[r][c] + 1
                q.append([x, y])
        
        return mat
