class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = {}
        for num in nums:
            ans[num] = ans.get(num, 0) + 1
        
        sorted_keys = sorted(ans.keys(), key=lambda x: ans[x], reverse=True)
        
        return sorted_keys[:k]