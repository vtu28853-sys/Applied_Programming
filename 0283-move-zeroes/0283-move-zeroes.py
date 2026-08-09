from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert_pos = 0
        
        # Iterate through the array
        for i in range(len(nums)):
            # If the current number is not zero
            if nums[i] != 0:
                # Swap the current number with the number at insert_pos
                # Only swap if they are different positions to minimize operations
                if i != insert_pos:
                    nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
                
                # Move the insert_pos pointer forward
                insert_pos += 1