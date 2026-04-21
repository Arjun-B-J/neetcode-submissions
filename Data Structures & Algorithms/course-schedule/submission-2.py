class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        
        visit = set()
        done = set()
        def dfs(crs):
            if crs in visit:
                return False
            if preMap[crs] == []:
                return True
            visit.add(crs)
            done.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            preMap[crs] = []
            return True

        for i in range(numCourses):
            if i not in done and not dfs(i):
                return False
        return True


