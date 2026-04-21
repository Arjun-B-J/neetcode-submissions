class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]!= ".":
                    if board[i][j] in columns[j]:
                        return False
                    if board[i][j] in rows[i]:
                        return False
                    if board[i][j] in boxes[(i//3)*3 + (j//3)]:
                        return False
                    columns[j].add(board[i][j])
                    rows[i].add(board[i][j])
                    boxes[(i//3)*3 + (j//3)].add(board[i][j])
        return True
        