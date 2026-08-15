class MyQueue:
    def __init__(self):
        self.input_stack = []   # Stack for pushing elements
        self.output_stack = []  # Stack for popping/peeking elements

    def push(self, x: int) -> None:
        """Pushes element x to the back of the queue."""
        self.input_stack.append(x)

    def _transfer(self):
        """Moves elements from input_stack to output_stack if output_stack is empty."""
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())

    def pop(self) -> int:
        """Removes the element from the front of the queue and returns it."""
        self._transfer()
        return self.output_stack.pop()

    def peek(self) -> int:
        """Returns the element at the front of the queue."""
        self._transfer()
        return self.output_stack[-1]

    def empty(self) -> bool:
        """Returns true if the queue is empty, false otherwise."""
        return not self.input_stack and not self.output_stack