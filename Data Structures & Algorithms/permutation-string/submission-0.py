class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 边界条件
        if len(s1) > len(s2):
            return False
            
        i = 0
        # 一直 i++ 直到结尾（留出 s1 的长度空间）
        while i <= len(s2) - len(s1):
            
            # 如果在 s2 中找到了 s1 里面的字符，直接进入搜寻模式
            if s2[i] in s1:
                # 截取 s1 长度的 substring
                s4 = s2[i : i + len(s1)]
                
                # 创建一个 temp 的 s1 字符串
                temp = s1
                match = True
                
                # 一个个找，一个个删除
                for j in range(len(s4)):
                    char_to_remove = s4[j]
                    
                    if char_to_remove in temp:
                        # 在 temp 中删除这个字符（只删除一个，count=1）
                        temp = temp.replace(char_to_remove, "", 1)
                    else:
                        # 发现不存在或者已经被删光了，说明不匹配
                        match = False
                        break
                
                # 如果最后 temp string 没了（删完了/为空），那就是完全重合的
                if match and len(temp) == 0:
                    return True
            
            # 无论成功与否，正常向前推进指针
            i += 1
            
        return False