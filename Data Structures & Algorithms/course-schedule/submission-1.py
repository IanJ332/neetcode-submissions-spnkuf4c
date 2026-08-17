class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. 建立邻接表 (Adjacency List)
        # 每个课程对应一个列表，存储它的所有先修课程
        adj = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        # 2. 状态集合
        visiting = set()  # 当前 DFS 路径上的节点（用于抓环 🔄）
        safe = set()      # 已经确认安全的节点（用于剪枝加速 ⚡）

        # 3. DFS 辅助函数
        def dfs(curr: int) -> bool:
            # 实现基础情况检查 (Base Cases)
            if curr in visiting:
                return False
            if curr in safe:
                return True
            # TODO: 标记当前节点为 visiting
            visiting.add(curr)
            # TODO: 递归检查所有先修课程
            for course in adj[curr]:
                if not dfs(course):
                    return False
            
            # TODO: 回溯，将当前节点从 visiting 移除，并加入 safe
            visiting.remove(curr)
            safe.add(curr)
            return True

        # 4. 主循环：遍历所有课程，依次做 DFS 检查
        for c in range(numCourses):
            if not dfs(c):
                return False

        return True