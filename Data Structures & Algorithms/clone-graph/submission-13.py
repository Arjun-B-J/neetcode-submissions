"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:

    def cloneNode(self,node,nodeMap):
        if node.val not in nodeMap:
            nodeMap[node.val] = Node(node.val)
        for ele in node.neighbors:
            if ele.val not in nodeMap:
                nodeMap[ele.val] = Node(ele.val)
            if nodeMap[ele.val] not in nodeMap[node.val].neighbors:
                nodeMap[node.val].neighbors.append(nodeMap[ele.val])
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        visit = set()
        q = deque()
        q.append(node)
        visit.add(node)
        nodeMap = {}
        self.cloneNode(node,nodeMap)
        while q:
            cur = q.popleft()
            for nxt in cur.neighbors:
                if nxt not in visit:
                    visit.add(nxt)
                    self.cloneNode(nxt,nodeMap)
                    q.append(nxt)
        return nodeMap[node.val]








                