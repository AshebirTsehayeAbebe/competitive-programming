from typing import List
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)  % 2 !=0 and len(changed)==0:
            return []
        output = []
        changed.sort()
        frequencyNumber = [0] *(2*changed[len(changed)-1]+1) 
        for i in changed:
            frequencyNumber[i]+=1
        for i in changed:
            if frequencyNumber[i]>0:                
                frequencyNumber[i]-=1
                if frequencyNumber[2*i]>0:
                   frequencyNumber[2*i]-=1        
                   output.append(i)
                else:
                    return []
        return output
    
obj = Solution()
n = int(input('Enter size: '))
changed = list(map(int, input("\nEnter the elements : ").strip().split()))[:n]
print(obj.findOriginalArray(changed))
