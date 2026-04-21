class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix is None or len(matrix) == 0:
            return -1
        L=0
        m = len(matrix[0])
        n = len(matrix)
        R = m*n - 1
        while(L<=R):
            mid = (L+R)//2
            firstIndex = max(0,(mid//m))
            secondIndex = mid%(m)
            if target > matrix[firstIndex][secondIndex]:
                L = mid+1
            elif target < matrix[firstIndex][secondIndex]:
                R = mid-1
            else:
                return True
        return False     