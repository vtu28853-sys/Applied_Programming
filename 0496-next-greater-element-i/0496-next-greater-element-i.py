from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Dictionary to store the next greater element for each number in nums2
        next_greater = {}
        stack = []
        
        # Iterate through nums2 to find next greater elements
        for num in nums2:
            # While stack is not empty and current num is greater than the top of the stack
            while stack and num > stack[-1]:
                # Pop the element and record its next greater element
                next_greater[stack.pop()] = num
            # Push current number onto the stack
            stack.append(num)
        
        # For elements remaining in stack, they have no next greater element, so map to -1
        while stack:
            next_greater[stack.pop()] = -1
            
        # Build the result for nums1 using the map
        return [next_greater[num] for num in nums1]