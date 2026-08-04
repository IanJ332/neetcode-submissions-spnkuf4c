class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        def dfs(index, path):
            if len(path) == len(digits):
                res.append(path)
                return

            for char in digitToChar[digits[index]]:
                dfs(index + 1, path + char)
        dfs(0, "")
        return res
