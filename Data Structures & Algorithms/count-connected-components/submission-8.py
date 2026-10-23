class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        complement= 0
        visited = set()
        adj = {}
        for j in range(n):
            adj[j] = []
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        def dfs(node):
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        for i in range(n):
            if i not in visited:
                visited.add(i)
                complement += 1
                dfs(i)
        return complement

    
        