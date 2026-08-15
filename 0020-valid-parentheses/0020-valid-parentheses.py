class Solution:
    def isValid(self, s: str) -> bool:
        # Map closing brackets to their corresponding opening brackets
        bracket_map = {')': '(', ']': '[', '}': '{'}
        stack = []

        for char in s:
            if char in bracket_map:
                # It's a closing bracket
                # Check if stack is empty or top doesn't match
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()  # Match found, pop the opening bracket
            else:
                # It's an opening bracket, push to stack
                stack.append(char)

        # If stack is empty, all brackets were matched correctly
        return not stack