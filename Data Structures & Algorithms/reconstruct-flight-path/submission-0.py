class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort()
        for src,dst in tickets:
            adj[src].append(dst)
        
        res = ["JFK"]
        def dfs(src):
            if len(res)==len(tickets)+1:
                return True
            if src not in adj:
                return False
            
            temp = list(adj[src])
            for index,dst in enumerate(temp):
                adj[src].pop(index)
                res.append(dst)
                if dfs(dst):
                    return True
                adj[src].insert(index,dst)
                res.pop()
        
        dfs("JFK")
        return res