class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for s in tokens: # 1. 修正：遍历对象改为 tokens
            if s in ["+", "-", "*", "/"]:
                num2 = stack.pop() # 先弹出的是右操作数 (Right operand)
                num1 = stack.pop() # 后弹出的是左操作数 (Left operand)
                
                # 4. 填补：加减乘除的 Case
                if s == "+":
                    res = num1 + num2
                elif s == "-":
                    res = num1 - num2
                elif s == "*":
                    res = num1 * num2
                elif s == "/":
                    # 使用 int() 实现向零截断 (Truncate toward zero)
                    res = int(num1 / num2) 
                
                # 将计算结果压回栈中
                stack.append(res)
            else:
                # 如果不是运算符，说明是数字，直接转成 int 压栈
                stack.append(int(s))
                
        # 5. 修正：整个 tokens 遍历完后，栈顶元素就是最终答案
        return stack[0]