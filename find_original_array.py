class Solution:
    def findOriginalArray(self, changed):
        output = []
        changed.sort()
        freNumber = [0] *(changed[len(changed)-1]+1) 
        if len(changed)  % 2 !=0 and len(changed)==0:
            return []
        for i in changed:
            freNumber[i]+=1
        for i in changed:
            if freNumber[i]>0:                
                freNumber[i]-=1
                if 2*i in changed: 
                    if freNumber[2*i]>0:
                       freNumber[2*i]-=1          
                       output.append(i)
                    else:
                        return []
        if len(output)!=len(changed)/2:
            return []
        return output
obj = Solution()
size = int(input('Enter size: '))
doubleArray = list(map(int, input("\nEnter the elements : ").strip().split()))[:size]
print(doubleArray)
originalArray = obj.findOriginalArray(doubleArray)
print(originalArray)
