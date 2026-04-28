class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        colors = [0] * n   # 0 = White, 1 = Gray, 2 = Black
        safe = []

        def dfs(node: int) -> bool:
            if colors[node] == 1:   # cycle detected
                return False
            if colors[node] == 2:   # already safe
                return True

            colors[node] = 1  # mark Gray (visiting)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            colors[node] = 2  # mark Black (safe)
            return True

        for i in range(n):
            if dfs(i):
                safe.append(i)

        return safe