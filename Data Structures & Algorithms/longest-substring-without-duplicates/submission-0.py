class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            # 💡 请在这里补全核心逻辑：
            # 1. 如果当前字符 s[right] 已经在 char_map 中，更新 left 的位置
            if s[right] in char_map:
                left = max(left, char_map[s[right]] + 1)
            # 2. 把当前字符和它的索引放进（或更新进）char_map
            char_map[s[right]] = right
            # 3. 计算当前窗口长度，并尝试更新 max_len
            max_len = max(max_len, right - left + 1)
        return max_len