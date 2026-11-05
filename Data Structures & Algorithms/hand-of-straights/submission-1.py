class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False
        count = len(hand) // groupSize
        count = collections.Counter(hand)
        
        x = min(hand)

        for x in sorted(count):
            if count[x] == 0:
                continue  # ⏭️ 已被消耗完，跳过
            
            k = count[x]  # 🎴 当前最小牌还剩 k 张，需要组 k 个顺子
            for i in range(groupSize):
                card = x + i
                if count[card] < k:
                    return False  # 🛑 顺子中断，无法凑齐
                count[card] -= k  # 📉 批量扣减
        return True