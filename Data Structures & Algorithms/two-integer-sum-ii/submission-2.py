class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers)-1
        tempSum = 0
        while(L<R):
            tempSum = numbers[L] + numbers[R]
            if  tempSum == target:
                return [L+1,R+1]
            elif tempSum>=target:
                R-=1
            else:
                L+=1
        return []
                
            
        