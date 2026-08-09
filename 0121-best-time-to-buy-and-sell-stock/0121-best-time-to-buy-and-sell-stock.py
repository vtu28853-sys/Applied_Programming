from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            # If current price is lower than min_price, update min_price
            if price < min_price:
                min_price = price
            # Otherwise, calculate profit and update max_profit if higher
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit
                    
        return max_profit