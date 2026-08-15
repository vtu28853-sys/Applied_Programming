class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []  # To store indices of '('
        to_remove = set()  # Indices to remove
        
        # First pass: Identify invalid ')' and match '('
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()  # Match found
                else:
                    to_remove.add(i)  # Unmatched ')'
        
        # Any indices left in stack are unmatched '('
        to_remove.update(stack)
        
        # Build the result string, skipping removed indices
        result = []
        for i, char in enumerate(s):
            if i not in to_remove:
                result.append(char)
        
        return "".join(result)