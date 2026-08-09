from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                # Swap nums[low] and nums[mid]
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 2:
                # Swap nums[mid] and nums[high]
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
                # Do not increment mid here, we need to check the new element
            else:
                # nums[mid] == 1
                mid += 1