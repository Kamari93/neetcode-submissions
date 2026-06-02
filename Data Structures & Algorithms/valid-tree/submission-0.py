class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def find_parent(node):
            if parent[node] != node:
                parent[node] = find_parent(parent[node])
            return parent[node]
        
        parent = list(range(n))
        components = n

        for a, b in edges:
            root_a = find_parent(a)
            root_b = find_parent(b)
        
            if root_a == root_b:
                return False
            
            parent[root_a] = root_b
            components -= 1
        
        return components == 1