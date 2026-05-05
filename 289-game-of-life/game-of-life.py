class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        directions = [(-1,-1), (-1,0), (-1,1),
                      (0,-1),         (0,1),
                      (1,-1),  (1,0), (1,1)]
        
        for i in range(m):
            for j in range(n):
                live = 0
                
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n:
                        if abs(board[ni][nj]) == 1:
                            live += 1
                
                if board[i][j] == 1:
                    if live < 2 or live > 3:
                        board[i][j] = -1
                else:
                    if live == 3:
                        board[i][j] = 2
        
        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0