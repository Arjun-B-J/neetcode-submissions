class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        for i in range(len(strs[0])):
            common += strs[0][i]
            for strings in strs:
                if not common in strings:
                    return common[:-1]
        return common 
