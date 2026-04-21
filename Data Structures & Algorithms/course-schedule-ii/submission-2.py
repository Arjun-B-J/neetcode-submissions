# Time Complexity: O(V + E) - We process every course (V) and every prerequisite edge (E) exactly once.
# Space Complexity: O(V + E) - Space for the adjacency list O(E), indegree array O(V), and the queue/output O(V).
# Approach: Breadth-First Search (Kahn's Algorithm for Topological Sorting)

import collections
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}          # Map prerequisite -> list of dependent courses
        indegree = [0] * numCourses                       # Tracks how many prerequisites a course still needs

        for u, v in prerequisites:
            adj[v].append(u)                              # Directed edge: finishing 'v' unlocks 'u'
            indegree[u] += 1                              # Course 'u' has one more prerequisite to satisfy

        # Start with the base layer: courses that require ZERO prerequisites
        queue = collections.deque([i for i in range(numCourses) if indegree[i] == 0])
        topSort = []                                      # Will store our valid course sequence

        while queue:
            current = queue.popleft()                     # "Take" the available course
            topSort.append(current)                       # Add it to our official schedule
            
            for next_course in adj[current]:              # Look at all courses that depend on this one
                indegree[next_course] -= 1                # Satisfy one of their prerequisites
                
                if indegree[next_course] == 0:            # If ALL prerequisites are met, it's ready to take
                    queue.append(next_course)
                    
        # If we took all courses, return the schedule. Otherwise, a cycle trapped us (return empty list)
        return topSort if len(topSort) == numCourses else []