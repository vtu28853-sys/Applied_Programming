# Definition for singly-linked list node.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # Phase 1: Detect if there is a cycle
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next          # Move 1 step
            fast = fast.next.next     # Move 2 steps
            
            if slow == fast:          # Cycle detected
                break
        else:
            return None  # No cycle found (fast reached the end)
        
        # Phase 2: Find the start of the cycle
        # Reset slow to head, keep fast at meeting point
        # Move both 1 step at a time until they meet
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow  # This is the start of the cycle