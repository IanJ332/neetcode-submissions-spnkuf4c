class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        maxArea = 0
        stack = [] # 存储 (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                # 栈顶柱子找到了右边界
                index, height = stack.pop()
                # 计算面积：宽度 = 当前索引 - 该柱子能追溯到的最左索引
                maxArea = max(maxArea, height * (i - index))
                # 既然当前柱子 h 比较矮，它可以向左延伸到刚才弹出的柱子的位置
                start = index
            stack.append((start, h))

        # 处理最后留在栈里的柱子（它们能一直延伸到最右端）
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
            
        return maxArea