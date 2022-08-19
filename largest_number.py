from typing import List
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        output=''
        for i in range(len(nums)):
            nums[i]=str(nums[i])
        self.mergeSort(nums)
        output=''.join(nums)
        if(output=='0'*len(output)):
            return '0'
        return output
    def mergeSort(self, nums):
        if len(nums)>1:
            mid=len(nums)//2
            Left=nums[:mid]
            Right=nums[mid:]
            self.mergeSort(Left)
            self.mergeSort(Right)
            
            i=j=k=0
            
            while i<len(Left) and j<len(Right):
                if Left[i]+Right[j]>Right[j]+Left[i]:
                    nums[k]=Left[i]
                    i+=1
                else:
                    nums[k]=Right[j]
                    j+=1
                k+=1
            
            
            while i<len(Left):
                    nums[k]=Left[i]
                    i+=1
                    k+=1
                  
            while j<len(Right):
                    nums[k]=Right[j]
                    j+=1
                    k+=1
  
obj = Solution()
n = int(input("Enter number of elements : "))   
elements = list(map(int,input("\nEnter the elements : ").strip().split()))[:n]
print(obj.largestNumber(elements))