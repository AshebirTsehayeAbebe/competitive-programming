from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
            dictionary={}
            answer=0
            for index, item in enumerate(nums):
                difference=k-item
                if difference in dictionary and dictionary[difference]>0:
                    answer+=1
                    dictionary[difference]-=1
                else:
                    if item not in dictionary:
                        dictionary[item]=0
                    dictionary[item]+=1
                    
                    
            return  answer

obj=Solution()
n=int(input('Enter array size: '))
nums = list(map(int,input('Enter array elements: ').strip().split()[:n]))

k=int(input('Enter the target number: '))

print(obj.maxOperations(nums, k))