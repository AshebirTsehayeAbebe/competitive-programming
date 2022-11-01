class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited=set()
        q=deque()
        q.append(start)
        visited.add(start)
        while q:
            curr=q.popleft()            
            if arr[curr]==0:
                return True
            if curr+arr[curr]<len(arr) and (curr+arr[curr]) not in visited:
                q.append(curr+arr[curr])
                visited.add(curr+arr[curr])
            if curr-arr[curr]>=0 and (curr-arr[curr]) not in visited:
                q.append(curr-arr[curr])
                visited.add(curr-arr[curr])
        return False 
