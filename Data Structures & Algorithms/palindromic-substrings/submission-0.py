class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(left, right):
            counter = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:   
                counter += 1
                left -= 1
                right += 1
            return counter
        ans = 0
        for i in range(len(s)):
            ans += expand(i, i)
            ans += expand(i, i + 1)
        return ans
