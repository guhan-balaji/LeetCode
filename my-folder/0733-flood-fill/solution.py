class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        return self.rec_fill(image, sr, sc, image[sr][sc], color)


    def rec_fill(self, img: List[List[int]], r: int, c: int, org_color: int, new_color: int) -> Optional[List[List[int]]]:
        if r >= len(img) or c >= len(img[0]) or r < 0 or c < 0:
            return
        
        elif img[r][c] == org_color and img[r][c] != new_color:
            img[r][c] = new_color

            self.rec_fill(img, r - 1, c, org_color, new_color)
            self.rec_fill(img, r, c - 1, org_color, new_color)
            self.rec_fill(img, r, c + 1, org_color, new_color)
            self.rec_fill(img, r + 1, c, org_color, new_color)

        return img
        
        
