class Trinode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = Trinode()
        
    def addWord(self, word: str) -> None:
        # 指向当前的root位置
        curr = self.root
        # 一个个添加
        for char in word:
            # 如果下一个位置不存在，那么就造一个trinode先
            if char not in curr.children:
                curr.children[char] = Trinode()
            # 放入tree中
            curr = curr.children[char]
        # 设置一下，把当前node的属性改为end，这样就知道它上面连起来是一个单词
        curr.is_end = True    

    def search(self, word: str) -> bool:
        

        def dfs(node, i):
            if i == len(word):
                return node.is_end
            
            char = word[i]

            # 如果当前的char是 . 那么就要用dfs往下看是不是对的
            if char == '.':
                # 一个个往下找
                for child in node.children.values():
                    # 判断条件
                    if dfs(child, i+1):
                        return True
                    # 如果搞完了发现还是没有返回就说明当前撞到墙了，返回错误
                return False
            # 普通字符捕获
            else:
                if char not in node.children:
                    return False
                return dfs(node.children[char], i + 1)
        return dfs(self.root, 0)



        
