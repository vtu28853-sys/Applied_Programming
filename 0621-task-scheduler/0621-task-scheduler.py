from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count frequency of each task
        freq = Counter(tasks)
        
        # Find the maximum frequency
        max_freq = max(freq.values())
        
        # Count how many tasks have this maximum frequency
        max_count = sum(1 for f in freq.values() if f == max_freq)
        
        # Calculate the number of "idle slots" required
        # We have (max_freq - 1) groups of tasks
        # Each group needs 'n' slots (some might be filled by other tasks, others idle)
        # The last group doesn't need idle time after it
        
        # Total slots needed = (max_freq - 1) * (n + 1) + max_count
        # This represents the structure: [MaxTask, others, idle..., MaxTask, others, idle...]
        num_slots = (max_freq - 1) * (n + 1) + max_count
        
        # The answer is the maximum of:
        # 1. The calculated slots (which includes idles)
        # 2. The total number of tasks (if no idles are needed because we have enough different tasks)
        return max(num_slots, len(tasks))