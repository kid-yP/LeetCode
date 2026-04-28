class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:        
        adj = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses
        
        for a, b in prerequisites:
            adj[b].append(a)
            indeg[a] += 1
        
        q = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        
        res = []
        
        while q:
            u = q.popleft()
            res.append(u)
            
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        
        return res if len(res) == numCourses else []