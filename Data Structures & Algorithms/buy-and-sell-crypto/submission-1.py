class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                current_profit = price - min_price
                max_profit = max(current_profit, max_profit)

        return max_profit
            