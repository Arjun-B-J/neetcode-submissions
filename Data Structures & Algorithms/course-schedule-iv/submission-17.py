class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for pre,crs in prerequisites:
            adj[crs].append(pre)
        prereqHashMap = {}

        def dfs(src):
            if src not in prereqHashMap:
                prereqHashMap[src] = set()
                for nei in adj[src]:
                    prereqHashMap[src] |= dfs(nei)  #union all prereq -> O(n)
                prereqHashMap[src].add(src)
            return prereqHashMap[src]
        
        #Build the pre req Hash map
        for crs in range(numCourses):
            dfs(crs)
        
        ans = []
        for pre,crs in queries:
            ans.append(pre in prereqHashMap[crs])
        return ans