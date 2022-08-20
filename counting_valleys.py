import string

class Solution:
    def countingValleys(self, steps, path):
        up, down, numberOfValleys, previousDown=0,0,0,0
        for element in path:        
            previousDown=down
            if element=='U':
                up+=1
                down-=1
            if element=='D':
                up-=1
                down+=1
            if previousDown>0 and down==up:
                numberOfValleys+=1
        return numberOfValleys

obj = Solution()
size = int(input('Enter size: '))
elements = list(input('Enter elements: '))
print(obj.countingValleys(size, elements))