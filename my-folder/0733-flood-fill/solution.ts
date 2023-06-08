function floodFill(image: number[][], sr: number, sc: number, color: number): number[][] {

    fill(image, sr, sc, image[sr][sc], color);

    return image;
};

function fill(img: number[][], sr: number, sc: number, init: number, color: number): void {
    if (sr < 0 || sc < 0 ||
        sr >= img.length || sc >= img[0].length || 
        img[sr][sc] !== init || img[sr][sc] === color) {
            return;
        }

 
    img[sr][sc] = color;

    fill(img, sr - 1, sc, init, color);
    fill(img, sr + 1, sc, init, color);
    fill(img, sr, sc - 1, init, color);
    fill(img, sr, sc + 1, init, color);
}
