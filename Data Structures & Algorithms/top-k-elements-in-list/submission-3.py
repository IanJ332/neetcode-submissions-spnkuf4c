class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_hash = {}
        for num in nums:
            if num not in num_hash:
                num_hash[num] = 1
            else:
                num_hash[num] += 1
        ans = sorted(num_hash.keys(), key = lambda x : num_hash[x], reverse = True)
        return ans[:k]