from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert_pos = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                # If the current position is different from where we want to place it, swap
                if i != insert_pos:
                    nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
                insert_pos += 1