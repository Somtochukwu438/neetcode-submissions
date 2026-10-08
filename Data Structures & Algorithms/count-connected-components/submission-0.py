class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))  # We start with n=5
        components = n
        
        # THE CHAIN OF COMMAND FINDER
        def find(node):
            while node != parent[node]:  # "Am I my own boss?"
                node = parent[node]      # "No? Let me go ask my boss."
            return node                  # "Yes! I am the ultimate boss."
            
        # PROCESS THE EDGES
        for node1, node2 in edges:
            boss1 = find(node1)
            boss2 = find(node2)
            
            if boss1 != boss2:           # "Are they on different teams?"
                parent[boss2] = boss1    # "Yes. Make boss1 the new boss of boss2."
                components -= 1          # "We just merged two teams, so total teams goes down by 1."
                
        return components
        