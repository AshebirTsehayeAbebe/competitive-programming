class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        visited = set()
        def dfs(node):
            for nei, adj in enumerate(isConnected[node]):
                if adj and nei not in visited:
                    visited.add(nei)
                    dfs(nei)

        ans = 0
        for i in range(N):
            if i not in visited:
                dfs(i)
                ans += 1
        return ans
                
                
