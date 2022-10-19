class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startColor=image[sr][sc]
        rowSize=len(image)
        colSize=len(image[0])
        in_bound= lambda row, col: 0<=row<rowSize and 0<=col<colSize
        def helper(row, col):
            if not in_bound(row, col) or image[row][col]!=startColor:
                return
            image[row][col]=color
            
            helper(row+1,col)
            helper(row-1,col)
            helper(row,col+1)
            helper(row,col-1)
            
        if startColor!=color:
            helper(sr, sc)
        return image
