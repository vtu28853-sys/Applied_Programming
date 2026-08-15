from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count frequency of each task
        freq = Counter(tasks)
        
        # Find the maximum frequency among all tasks
        max_freq = max(freq.values())
        
        # Count how many tasks have this maximum frequency
        max_count = sum(1 for f in freq.values() if f == max_freq)
        
        # Calculate the minimum slots required based on the bottleneck task
        # Structure: [MaxTask, others, idle..., MaxTask, others, idle..., MaxTask]
        # Number of full groups = (max_freq - 1)
        # Size of each group = (n + 1)
        # Remaining slots for the last group = max_count
        num_slots = (max_freq - 1) * (n + 1) + max_count
        
        # The answer is the maximum of:
        # 1. The calculated slots (which accounts for mandatory idle times)
        # 2. The total number of tasks (if we have enough different tasks to fill all idle slots)
        return max(num_slots, len(tasks))