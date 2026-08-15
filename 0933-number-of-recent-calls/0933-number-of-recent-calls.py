from collections import deque

class RecentCounter:
    def __init__(self):
        self.queue = deque()
    
    def ping(self, t: int) -> int:
        self.queue.append(t)
        # Remove all pings older than 3000ms from the current time t
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)