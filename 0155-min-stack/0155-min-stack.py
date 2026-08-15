class MinStack:
    def __init__(self):
        self.stack = []       # Main stack to store values
        self.min_stack = []   # Stack to store minimum values

    def push(self, value: int) -> None:
        self.stack.append(value)
        # Push to min_stack if it's empty or the new value is <= current min
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            # If the popped value is the current min, pop from min_stack too
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]