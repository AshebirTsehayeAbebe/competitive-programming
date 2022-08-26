class Solution:    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key = lambda l:l[0])
        print(intervals)
        for i in range(len(intervals)):
            if i == 0:
                result.append(intervals[i])
                continue

            lastInterval = result[len(result) - 1]
            if lastInterval[1] < intervals[i][0]:
                result.append(intervals[i])
            elif lastInterval[1] >= intervals[i][0]:
                lastInterval[1] = max(intervals[i][1],lastInterval[1])

        return result;
        
input = [[1,3],[2,6],[8,10],[15,18]]   
output = merge(input)
print(output)
