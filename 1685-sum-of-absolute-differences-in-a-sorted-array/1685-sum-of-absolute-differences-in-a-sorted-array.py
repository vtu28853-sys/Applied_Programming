from typing import List

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total_sum = sum(nums)
        result = [0] * n
        
        left_sum = 0
        
        for i in range(n):
            # Calculate the sum of absolute differences on the left
            # left_sum is the sum of nums[0]...nums[i-1]
            # The contribution from the left is: (nums[i] * i) - left_sum
            left_diff = (nums[i] * i) - left_sum
            
            # Calculate the sum of absolute differences on the right
            # right_sum is the sum of nums[i+1]...nums[n-1]
            # We can find right_sum using: total_sum - left_sum - nums[i]
            right_sum = total_sum - left_sum - nums[i]
            
            # The contribution from the right is: right_sum - (nums[i] * (n - 1 - i))
            right_diff = right_sum - (nums[i] * (n - 1 - i))
            
            result[i] = left_diff + right_diff
            
            # Update left_sum for the next iteration
            left_sum += nums[i]
            
        return result