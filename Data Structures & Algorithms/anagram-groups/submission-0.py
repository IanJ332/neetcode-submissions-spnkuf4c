from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 使用 defaultdict，键是频率元组，值是包含异位词的列表
        # 元组 (tuple) 是不可变的，所以可以用作字典的键
        anagram_groups = defaultdict(list)
        
        for s in strs:
            # 初始化一个长度为 26 的列表或数组来存储 a-z 的频率
            count = [0] * 26
            
            # 遍历字符串 s，计算频率
            for char in s:
                # ord(char) - ord('a') 得到字符在字母表中的索引 (0-25)
                count[ord(char) - ord('a')] += 1
            
            # 将列表转换为元组作为字典的键，因为列表是可变的，不能作为键
            key = tuple(count)
            
            # 将字符串添加到对应键的值列表
            anagram_groups[key].append(s)
            
        # 返回字典中所有的值，即所有异位词分组
        return list(anagram_groups.values())