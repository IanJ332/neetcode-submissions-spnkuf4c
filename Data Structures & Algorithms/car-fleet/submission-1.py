class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # 1. 将位置和速度打包，并按位置从大到小（从右向左）排序
        cars = sorted(zip(position, speed), reverse = True)
        
        # 2. 计算每辆车独立到达终点的时间（使用浮点数除法 /）
        times = [(target - p) / s for p, s in cars]
        
        stack = []
        for t in times:
            # 💡 请根据刚才的结论，补全这里的栈操作逻辑：
            # 如果栈为空，或者当前车的时间 t 大于栈顶车的时间（追不上）
            if not stack or t > stack[-1]:
                stack.append(t)
            # 如果 t <= stack[-1]（能追上），我们需要做什么吗？
                

        return len(stack)