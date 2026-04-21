class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROW,COL = len(matrix),len(matrix[0])
        self.prefixM = [[0]*(COL+1) for _ in range(ROW+1)]
        for i in range(ROW):
            prefix=0
            for j in range(COL):
                prefix+=matrix[i][j]
                self.prefixM[i+1][j+1] = prefix+self.prefixM[i][j+1]

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1+=1
        col1+=1
        row2+=1
        col2+=1
        bottom = self.prefixM[row2][col2]
        left = self.prefixM[row1-1][col2]
        up = self.prefixM[row2][col1-1]
        topleft= self.prefixM[row1-1][col1-1]
        return bottom -left-up+topleft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)