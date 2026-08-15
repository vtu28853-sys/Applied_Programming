class MyCircularDeque:
    def __init__(self, k: int):
        self.k = k
        self.queue = [None] * k
        self.head = 0
        self.tail = 0
        self.count = 0  # Tracks the number of elements currently in the deque

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        # Move head backwards (circularly)
        self.head = (self.head - 1 + self.k) % self.k
        self.queue[self.head] = value
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.k
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.k
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.tail = (self.tail - 1 + self.k) % self.k
        self.count -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        # tail points to the next empty spot, so the last element is at (tail - 1)
        return self.queue[(self.tail - 1 + self.k) % self.k]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k