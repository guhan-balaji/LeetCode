class Solution(object):
    def floodFill(self, image, sr, sc, color):
        self.rec_fill(image, sr, sc, color, image[sr][sc])
        return image

        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
    
    def rec_fill(self, image, sr, sc, color, org):
        if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]):
            return

        if image[sr][sc] == color or image[sr][sc] != org:
            return

        if image[sr][sc] == org:
            image[sr][sc] = color


        self.rec_fill(image, sr, sc - 1, color, org)
        self.rec_fill(image, sr, sc + 1, color, org)
        self.rec_fill(image, sr - 1, sc, color, org)
        self.rec_fill(image, sr + 1, sc, color, org)

