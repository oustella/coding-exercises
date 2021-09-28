from typing import List
class Solution:
    
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # if a cell '0' touches a boarder '0' then it cannot be flipped
        # all other '0' cells can be converted
        
        # mark all boarder cells with '0' and the cells they touch to temp
        for i in range(len(board)): # all rows
            for j in [0, len(board[0])-1]: # the first and last column
                if board[i][j] == 'O':
                    self.helper(board, i, j)
    
        for i in [0, len(board)-1]:  # the first and last row
            for j in range(len(board[0])): # all columns
                if board[i][j] == 'O':
                    self.helper(board, i, j)
                    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'temp':
                    board[i][j] = 'O'
    
    # recursively finding all cells connected to boarder "O"s
    def helper(self, board, i, j):
        if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == 'O':
            board[i][j] = 'temp'
            # recursion
            self.helper(board, i+1, j)
            self.helper(board, i-1, j)
            self.helper(board, i, j+1)
            self.helper(board, i, j-1)