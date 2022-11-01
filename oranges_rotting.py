class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue, cnt = deque(), 0
        in_bound=lambda r, c: 0<=r<m and 0<=c<n
        for i, j in product(range(m), range(n)):
                if grid[i][j] == 1:
                    cnt += 1
                if grid[i][j] == 2:
                    queue.append((i, j))
        if not queue:
            return -1 if cnt else 0
        res = -1
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                adj=[(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                for k, l in adj:
                    if in_bound(k, l) and grid[k][l] == 1:
                        queue.append((k, l))
                        grid[k][l] = 2
                        cnt-=1
            res += 1
        if cnt>0:
            return -1
        return res
