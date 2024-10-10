class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        if(image[sr][sc] == color)
            return image;
        int rows = image.length;
        int cols = image[0].length;
        int source = image[sr][sc];
        change(image, sr, sc, color, rows, cols, source);
        return image;
    }

    public void change(int[][] image, int sr, int sc, int newColor, int rows, int cols, int source){
        if(sr<0 || sr>=rows || sc <0 || sc >= cols)
            return;
        else if (image[sr][sc]!=source)
            return;
        
        image[sr][sc] = newColor;

        change(image,(sr+1),sc, newColor, rows, cols, source);
        change(image,(sr-1),sc, newColor, rows, cols, source);
        change(image,sr,sc+1, newColor, rows, cols, source);
        change(image, (sr),sc-1, newColor, rows, cols, source);
    }

}
