class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR
        # 任何数和 0 做XOR，结果还是它自己：a XOR 0 = a
        # 任何数和自己做异或，结果会“消消乐”变成 0：a XOR a = 0
        # 它满足交换律和结合律：a XOR b XOR a = (a XOR a) XOR b = 0 XOR b = b
        a = 0
        for num in nums:
            a = a ^ num
        return a
