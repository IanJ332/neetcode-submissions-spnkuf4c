class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 1. 建立邻接表
        adj = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            adj[course].append(pre)
        
        visiting = set()  # 正在当前递归路径上的节点（抓环 🔄）
        safe = set()      # 已经验证安全并加入结果的节点（剪枝 ⚡）
        res = []          # 最终的拓扑排序结果 📝

        def dfs(curr: int) -> bool:
            # 遇到环
            if curr in visiting:
                return False
            # 已经处理过，直接跳过
            if curr in safe:
                return True
            
            visiting.add(curr)
            for pre in adj[curr]:
                if not dfs(pre):
                    return False
            
            # 回溯：移出探索中集合，加入安全集合与结果列表
            visiting.remove(curr)
            safe.add(curr)
            res.append(curr)
            
            return True

        # 遍历所有课程
        for c in range(numCourses):
            if not dfs(c):
                return []
                
        return res