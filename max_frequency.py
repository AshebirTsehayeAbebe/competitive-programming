from collections import Counter
def maxFrequency(nums, k):
 if len(nums)==0:
  return 0
 numCounter = Counter(nums)
 sortedNums = sorted(numCounter.items(),key = lambda i: i[0])
 if len(sortedNums)==1:
  return sortedNums[0][1] 
 answer=1 
 for i in range(1, len(sortedNums)):
  count = 0
  tracker=i-1
  element = sortedNums[tracker][0]
  temAns = sortedNums[i][1]
  print(temAns)
  while count <= k and tracker>=0:
   if element==sortedNums[i][0]:
     temAns+=sortedNums[tracker][1]
     tracker-=1
     element = sortedNums[tracker][0]
     continue
   element+=1   
   count+=1
 answer=max(answer, temAns)
 return answer
elements  = list(map(int,input('Enter elements: ').strip().split()[:5]))
print(maxFrequency(elements, 5))
    