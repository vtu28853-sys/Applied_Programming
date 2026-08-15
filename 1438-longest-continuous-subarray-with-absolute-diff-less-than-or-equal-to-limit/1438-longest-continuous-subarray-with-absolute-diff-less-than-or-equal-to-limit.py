from collections import deque
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = deque()  # Stores indices of potential max values (decreasing)
        min_deque = deque()  # Stores indices of potential min values (increasing)
        left = 0
        max_len = 0
        
        for right, num in enumerate(nums):
            # Maintain max_deque: remove elements smaller than current from the back
            while max_deque and nums[max_deque[-1]] <= num:
                max_deque.pop()
            max_deque.append(right)
            
            # Maintain min_deque: remove elements larger than current from the back
            while min_deque and nums[min_deque[-1]] >= num:
                min_deque.pop()
            min_deque.append(right)
            
            # Shrink the window if the difference exceeds the limit
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                left += 1
                # Remove indices that are now out of the window
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()
            
            # Update the maximum length found so far
            max_len = max(max_len, right - left + 1)
        
        return max_len