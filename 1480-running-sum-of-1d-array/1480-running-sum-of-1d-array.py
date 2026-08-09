from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # Create a result list of the same length
        result = [0] * len(nums)
        
        # Initialize the first element
        result[0] = nums[0]
        
        # Iterate from the second element to the end
        for i in range(1, len(nums)):
            # Current running sum = previous running sum + current number
            result[i] = result[i - 1] + nums[i]
            
        return result