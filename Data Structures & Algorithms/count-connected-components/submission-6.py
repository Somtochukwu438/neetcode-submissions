class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        complement = n
        def find(node):
            while node != parent[node]:
                node = parent[node]
            return node
        
        for a, b in edges:
            boss1 = find(a)
            boss2 = find(b)

            if boss1 != boss2:
                parent[boss2] = boss1
                complement -= 1
        return complement
        