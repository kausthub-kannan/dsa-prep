class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def has_duplicates(lst):
            seen = set()
            for num in lst:
                if num != '.':
                    if num in seen:
                        return True
                    seen.add(num)
            return False

        def checkRow(row):
            return not has_duplicates(board[row])

        def checkColumn(col):
            column = [board[i][col] for i in range(9)]
            return not has_duplicates(column)

        def checkGrid(row, col):
            subgrid = [board[i][j] for i in range(row, row + 3) for j in range(col, col + 3)]
            return not has_duplicates(subgrid)

        for i in range(9):
            if not checkRow(i) or not checkColumn(i):
                return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not checkGrid(i, j):
                    return False

        return True

s = Solution()
s.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])

s.isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])

# Leetcode URL: https://leetcode.com/problems/valid-sudoku/description
