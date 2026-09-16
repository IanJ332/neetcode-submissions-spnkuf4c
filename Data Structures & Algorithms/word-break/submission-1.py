class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] 表示 s 的前 i 个字符是否可以被拆分
        dp = [False] * (len(s) + 1)
        dp[0] = True  # 基础状态：空字符串可以被拆分

        for i in range(1, len(s) + 1):
            for j in range(i):
                # 如果前 j 个字符合法，且剩下的切片也在字典中
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[-1]