class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # 1. 初始化 result 和 stack
        result = [0] * len(temperatures)
        stack = []
        # 2. 用 for 循环遍历每一个天气的索引 i 和温度 temp
        for i in range(len(temperatures)):
            # 3. 用 while 循环对比当前温度与栈顶温度
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            stack.append(i)
        # 4. 返回结果
        return result