class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def dfs(curr, parent):
            visited.add(curr)
            for nbr in adj[curr]:
                # 跳过父节点 因为它只是沿着无向边原路返回，不是环。
                if nbr == parent:
                    continue
                if nbr in visited:
                    return False
                if not dfs(nbr, curr):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n