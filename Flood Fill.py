class Solution:
    def change(self, image, sr, sc, newColor, rows, cols, source):
        if(sr<0 or sr>=rows or sc <0 or sc >= cols):
            return
        elif(image[sr][sc]!= source):
            return
        
        image[sr][sc] = newColor

        self.change(image, sr+1, sc, newColor, rows, cols, source)
        self.change(image, sr-1, sc, newColor, rows, cols, source)
        self.change(image, sr, sc+1, newColor, rows, cols, source)
        self.change(image, sr, sc-1, newColor, rows, cols, source)

    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if(image[sr][sc] == color):
            return image
        rows = len(image)
        cols = len(image[0])
        source = image[sr][sc]
        self.change(image, sr, sc, color, rows, cols, source)
        return image

    
