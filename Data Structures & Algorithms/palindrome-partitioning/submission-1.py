class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(sub):
            l, r = 0, len(sub) - 1
            while l < r:
                if sub[l] != sub[r]:
                    return False
                r -= 1
                l += 1
            return True

        def dfs(start, path):
            if start == len(s):
                res.append(path[:])
                return
            
            for i in range(start, len(s)):
                sub = s[start : i + 1]
                if isPalindrome(sub):
                    dfs(i + 1, path + [sub])

        dfs(0, [])
        return res