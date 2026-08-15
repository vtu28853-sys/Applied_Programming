from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        # Initialize result array with 0s (default if no warmer day is found)
        answer = [0] * n
        # Stack will store indices, not values, to calculate the day difference
        stack = []
        
        for i, temp in enumerate(temperatures):
            # While stack is not empty and current temp is warmer than the temp at stack top
            while stack and temperatures[stack[-1]] < temp:
                # Pop the index of the colder day
                prev_index = stack.pop()
                # Calculate the number of days to wait
                answer[prev_index] = i - prev_index
            
            # Push current index onto the stack
            stack.append(i)
            
        return answer