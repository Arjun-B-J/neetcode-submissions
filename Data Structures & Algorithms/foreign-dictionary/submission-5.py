class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for word in words for c in word}
        #build the adjaceny list with character dependecies
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            if len(w1)>len(w2) and w1[:len(w2)]==w2:
                return ""
            for j in range(min(len(w1),len(w2))):
                if w1[j]!=w2[j]:
                    adj[w1[j]].add(w2[j])
                    break #remember to break when we find the first diff
        

        def dfs(src,adj,path,visit)->bool: #if cycle False
            if src in path:
                return False
            if src in visit:
                return True
            visit.add(src)
            path.add(src)
            for nei in adj[src]:
                if not dfs(nei,adj,path,visit):
                    return False
            path.remove(src)
            topSort.append(src)
            return True

        path = set()
        visit = set()
        topSort = []
        for c in adj:
            if not dfs(c,adj,path,visit):
                print("here")
                return ""
        topSort.reverse()
        return "".join(topSort)


        
