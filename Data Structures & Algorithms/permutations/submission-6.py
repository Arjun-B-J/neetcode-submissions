class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = [[]]
        for num in nums:
            nextPermutation = []
            for p in permutations:
                for j in range(len(p)+1):
                    pCopy = p.copy()
                    pCopy.insert(j,num)
                    nextPermutation.append(pCopy)
            permutations = nextPermutation
        return permutations