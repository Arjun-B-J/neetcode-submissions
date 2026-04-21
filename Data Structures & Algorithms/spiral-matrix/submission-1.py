class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left,right=0,len(matrix[0])
        top,bottom=0,len(matrix)
        res = []
        while left<right and top<bottom:
            #travese top row, left to right
            for i in range(left,right):
                res.append(matrix[top][i])
                
            top+=1
            print(res,"1")
            #traverse right, top to bottom
            for i in range(top,bottom):
                res.append(matrix[i][right-1])
                
            right-=1
            print(res,"2")
            if not (left<right and top<bottom):
                break
            
            #traverse bottom, right to left
            for i in range(right-1,left-1,-1):
                res.append(matrix[bottom-1][i])
                
            bottom-=1
            print(res,"3")
            #travese left, bottom to top
            for i in range(bottom-1,top-1,-1):
                res.append(matrix[i][left])
                
            left+=1
            print(res,"4")
        return res




            