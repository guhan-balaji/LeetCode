class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def flood_fill(image: List[List[int]], r: int, c: int, color: int, start_color: int):
            if r < 0 or c < 0 or r >= len(image) or c >= len(image[0]):
                return
            
            elif image[r][c] == color:
                return
            
            elif image[r][c] == start_color:
                image[r][c] = color
                
                flood_fill(image, r - 1, c, color, start_color)
                flood_fill(image, r + 1, c, color, start_color)
                flood_fill(image, r, c - 1, color, start_color)
                flood_fill(image, r, c + 1, color, start_color)
                return
            
            else:
                return

        flood_fill(image, sr, sc, color, image[sr][sc])
        return image
        
