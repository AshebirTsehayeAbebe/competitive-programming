class Solution:
    def numberOfSquares(self,m: int, n: int, a: int)->int:
        
        widthCount=m//a
        columnCount = n//a
        
        if m%a != 0:
            widthCount+=1
        if n%a != 0: 
            columnCount+=1
        return widthCount*columnCount
