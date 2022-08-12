from re import L


def mergeSort(nums):
 if len(nums)>1:
  length=len(nums)
  medium=len(nums)//2
  L=nums[:medium]
  M=nums[medium:]
  
  mergeSort(L)
  mergeSort(M)
  
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
 
 
def sortColors(nums) -> None:
 mergeSort(nums) 
 for i in range(len(nums)):  
  print(nums[i])
nums=[2,1,0,2,1,2,0]
sortColors(nums)