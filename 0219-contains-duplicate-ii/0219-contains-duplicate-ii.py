from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        
        for i in range(len(nums)):
            # If the window size exceeds k, remove the oldest element
            if i > k:
                window.remove(nums[i - k - 1])
            
            # If the current number is already in the window, we found a duplicate
            if nums[i] in window:
                return True
            
            # Add the current number to the window
            window.add(nums[i])
            
        return False