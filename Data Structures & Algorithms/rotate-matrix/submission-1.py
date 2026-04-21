class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l,r = 0,len(matrix)-1
        while l<r:
            top,bottom = l,r
            for i in range(r-l):
                temp= matrix[top][l+i] #top left saving
                matrix[top][l+i] = matrix[bottom-i][l] #bottom left to top left
                matrix[bottom-i][l] = matrix[bottom][r-i] #bottom right to bottom left
                matrix[bottom][r-i] = matrix[top+i][r] #top right to bottom left
                matrix[top+i][r] = temp #top left to top right
            l+=1
            r-=1
        