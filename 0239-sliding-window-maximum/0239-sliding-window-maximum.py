from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        
        result = []
        # Deque stores indices of elements in nums
        # The values at these indices are in decreasing order
        dq = deque()
        
        for i, num in enumerate(nums):
            # Remove indices that are out of the current window from the front
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            
            # Remove indices of all elements from the back
            # that are smaller than or equal to the current element
            # because they are useless (current element is larger and newer)
            while dq and nums[dq[-1]] <= num:
                dq.pop()
            
            # Add current element's index to the deque
            dq.append(i)
            
            # The front of the deque is the index of the maximum element in the current window
            # Start adding to result once the first window is formed (i >= k - 1)
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result