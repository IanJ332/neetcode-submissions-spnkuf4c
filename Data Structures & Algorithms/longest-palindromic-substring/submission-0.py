class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        # 边界情况快速处理
        if n < 2:
            return s

        def expand(left: int, right: int):
            while left >= 0 and right <= n - 1 and s[left] == s[right]:
                left -= 1
                right += 1
            # 退出循环时超出了 1 步，收缩回有效边界
            return left + 1, right - 1

        start = 0
        end = 0
        max_len = 0

        for i in range(n):
            # 1. 尝试奇数长度扩展（以 i 为单中心）
            l1, r1 = expand(i, i)
            # 2. 尝试偶数长度扩展（以 i 和 i+1 为双中心）
            l2, r2 = expand(i, i + 1)

            # 更新奇数中心的最优解
            if r1 - l1 + 1 > max_len:
                max_len = r1 - l1 + 1
                start, end = l1, r1

            # 更新偶数中心的最优解
            if r2 - l2 + 1 > max_len:
                max_len = r2 - l2 + 1
                start, end = l2, r2

        # 切片左闭右开，截取到 end + 1
        return s[start : end + 1]