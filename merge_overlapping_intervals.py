def merge(intervals):
        output = []
        for i in range(1, len(intervals)):
            j=i-1
            key = intervals[i]
            
            while(j>=0 and key[0]<intervals[j][0]):
                intervals[j+1]=intervals[j]
                j-=1
            intervals[j+1]=key
        
        tempInterval=intervals[0]
        for currentInterval in intervals:
            if currentInterval[0]<=tempInterval[1]:
                tempInterval[1]=max(tempInterval[1], currentInterval[1])
            else:
                output.append(tempInterval)
                tempInterval=currentInterval
        print(intervals)     
        output.append(tempInterval)
        return output
        
input = [[1,3],[2,6],[8,10],[15,18]]   
output = merge(input)
print(output)