from typing import List
class Solution:  
    def pancakeSort(self, arr: List[int]) -> List[int]:
        output = []
        def flip(largestIndex):
            for i in range(0, largestIndex//2+1):
                tmp = arr[i]
                arr[i] = arr[largestIndex-i]
                arr[largestIndex-i] = tmp
        for i in range(len(arr)-1, 0, -1):
            for j in range(1, i+1):
                if arr[j] == i+1:
                    flip(j)
                    output.append(j+1)
                    break
            flip(i)
            output.append(i+1)
        return output
            
obj= Solution()
n=int(input('Enter input size: '))
arr=list(map(int,input('Enter array elements: ').strip().split()[:n]))
print(obj.pancakeSort(arr))
