from inspect import _void
from re import L
from typing import List
class Solution:
  def mergeSort(self, nums: List[int])->None:
    if len(nums)>1:
      length=len(nums)
      medium=len(nums)//2
      L=nums[:medium]
      M=nums[medium:]
      
      self.mergeSort(L)
      self.mergeSort(M)
      
      i=j=k=0
      
      while(i<len(L) and j<len(M)):
        if(L[i]<M[j]):
          nums[k]=L[i]
          i+=1
        else:
          nums[k]=M[j]
          j+=1
        k+=1
      
      while(i<len(L)):
        nums[k]=L[i]
        i+=1
        k+=1
        
      while(j<len(M)):
        nums[k]=M[j]
        j+=1
        k+=1
  
  
  def kthLargestNumber(self, nums: List[str], k: int) -> str:
   for i in range(len(nums)):
    nums[i]=int(nums[i])
   self.mergeSort(nums)
   return str(nums[len(nums)-k])
  
obj = Solution()

n = int(input("Enter array size : "))   
nums = list(map(str,input("\nEnter elements : ").strip().split()))[:n]
k = int(input("Enter  index: "))

print(obj.kthLargestNumber(nums, k))