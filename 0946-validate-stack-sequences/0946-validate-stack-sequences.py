from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pop_idx = 0
        
        for num in pushed:
            stack.append(num)
            
            # While the top of the stack matches the current element to pop
            while stack and stack[-1] == popped[pop_idx]:
                stack.pop()
                pop_idx += 1
        
        # If the stack is empty, the sequence is valid
        return not stack