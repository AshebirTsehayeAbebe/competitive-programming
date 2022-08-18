import math
def numberOfSquares(m, n, a):
    
    widthCount=m//a
    columnCount = n//a
    
    if m%a != 0:
        widthCount+=1
    if n%a != 0: 
        columnCount+=1
    return widthCount*columnCount
print(numberOfSquares(6, 6, 4))