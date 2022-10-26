class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n= len(board), len(board[0])
        visited = set()
        outside_border = lambda row, col: (row==0 or row==m-1) or (col==0 or col==n-1)
        def dfs(i, j):
            visited.add((i, j))
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for direction in directions: 
                new_r = i + direction[0]
                new_c = j + direction[1]
                if (0 <= new_r < len(board) and 0 <= new_c < len(board[i]) and board[new_r][new_c] == 'O' 
                and (new_r, new_c) not in visited):
                    dfs(new_r, new_c)
                    
        for i, j in product(range(m), range(n)):
                if board[i][j] == 'O' and outside_border(i, j):
                    dfs(i, j)
        
        for i, j in product(range(m), range(n)):
                if board[i][j] == 'O' and (i , j) not in visited: 
                    board[i][j] = 'X'
        
