from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []  # Stack stores indices of prices
        n = len(prices)
        result = prices.copy()  # Create a copy to store final prices

        for i in range(n):
            # While stack is not empty and current price is <= price at stack top
            while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()
                result[idx] -= prices[i]  # Apply discount
            stack.append(i)

        return result