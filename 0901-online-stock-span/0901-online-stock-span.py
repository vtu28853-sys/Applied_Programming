class StockSpanner:
    def __init__(self):
        # Each element is a tuple: (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        # Pop elements from the stack that are less than or equal to current price
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        # Push current price and its span to the stack
        self.stack.append((price, span))
        return span