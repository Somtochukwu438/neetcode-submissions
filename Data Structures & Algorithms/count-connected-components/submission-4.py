class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}        
        for i in range(n):
            adj[i] = []

        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        complement = 0
        visited = set()

        def dfs(node):
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)


        for j in range(n):
            if j not in visited:
                complement += 1
                visited.add(j)
                dfs(j)
        return complement
        