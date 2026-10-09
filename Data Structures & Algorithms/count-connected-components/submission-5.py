class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        complement = n

        def find(node):
            while node != parent[node]:
                node = parent[node]
            return node


        for node1, node2 in edges:
            boss1 = find(node1)
            boss2 = find(node2)

            if boss1 != boss2:
                parent[boss2] = boss1
                complement -= 1
        return complement
        