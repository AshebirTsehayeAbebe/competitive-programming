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
  
  
  def sortColors(self, nums) -> None:
    self.mergeSort(nums) 
    for i in range(len(nums)):  
      print(nums[i])
  
nums=[2,1,0,2,1,2,0]
obj = Solution()
obj.sortColors(nums)