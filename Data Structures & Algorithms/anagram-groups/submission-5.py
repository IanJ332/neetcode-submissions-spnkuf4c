class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_hash = {}
        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            if key in word_hash:
                word_hash[key].append(strs[i])
            else:
                word_hash[key] = [strs[i]]
        return list(word_hash.values())