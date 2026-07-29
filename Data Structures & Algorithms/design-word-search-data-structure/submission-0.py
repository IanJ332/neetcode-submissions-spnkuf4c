class TrieNode:

    def __init__(self):
        self.children = {}  # 🗂️ 存放字符到子节点的映射
        self.is_end = False  # 🏁 单词标记


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()  # 🌳 根节点

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True

    def search(self, word: str) -> bool:
        # 内部嵌套 DFS 函数 🔍
        def dfs(node, i):
            if i == len(word):
                return node.is_end

            char = word[i]

            if char == ".":
                for child in node.children.values():
                    if dfs(child, i + 1):  # 只要有一条路径成功就返回 True
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(node.children[char], i + 1)

        return dfs(self.root, 0)