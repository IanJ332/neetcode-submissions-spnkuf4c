class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = {i: i for i in range(1, n + 1)}
        
        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        for u, v in edges:
            root_u = find(u)
            root_v = find(v)
            
            # 如果根节点相同，说明形成了环，直接返回这条边
            if root_u == root_v:
                return [u, v]
            
            # 否则将两个圈子合并
            parent[root_u] = root_v