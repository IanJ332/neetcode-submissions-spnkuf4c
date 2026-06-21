class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        left = 0
        max_freq = 0
        
        for right in range(len(s)):
            # 1. 增加当前字符的计数，并更新 max_freq
            counts[s[right]] = counts.get(s[right], 0) + 1
            max_freq = max(max_freq, counts[s[right]])
            
            # 2. 如果窗口无效(可以替换的字符 > k值，也就是无法全部替换)
            # 假设现在还是AAABABB：
            #     我们走到第二个B的时候，发现当前right - left - max freq的时候
            #     也就是计算出**需要替换的字母** > 可替换字母次数k，的时候
            #     那么windows为无效的，所以必须要移动left，缩小窗口 
            if (right - left + 1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1
                
        # 3. 📊 遍历结束后，返回最长有效窗口的长度
        return right - left + 1