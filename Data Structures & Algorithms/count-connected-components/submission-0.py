class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i : [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v) 
            adj[v].append(u)
        res = 0
        visited = set()
        
        def dfs(curr):
            visited.add(curr)
            for nbr in adj[curr]:
                if nbr not in visited:
                    dfs(nbr)
                else:
                    continue
            
        for node in range(n):
            if node in visited:
                continue
            else:
                dfs(node)
                res += 1

        return res