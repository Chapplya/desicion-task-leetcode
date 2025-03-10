class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for row in range(9):
            set_check = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in set_check:
                    return False
                set_check.add(board[row][i])
        for clm in range(9):
            set_check = set()
            for i in range(9):
                if board[i][clm] == ".":
                    continue
                if board[i][clm] in set_check:
                    return False
                set_check.add(board[i][clm])
        for sqr in range(9):
            set_check = set()
            for i in range(3):
                for j in range(3):
                    row = (sqr // 3) * 3 + i
                    col = (sqr % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in set_check:
                        return False
                    set_check.add(board[row][col])
        return True


settings = Solution()

board = [
    ["1", "2", ".", ".", "3", ".", ".", ".", "."],
    ["4", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", ".", "3"],
    ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
    [".", ".", ".", "8", ".", "3", ".", ".", "5"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", ".", ".", ".", ".", ".", "2", ".", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "8"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

assert settings.isValidSudoku(board)


