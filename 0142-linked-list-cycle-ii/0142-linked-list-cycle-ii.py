# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Phase 1: Detect if there is a cycle
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                # Cycle detected, break to find the start
                break
        else:
            # If the loop completed without breaking, no cycle exists
            return None
        
        # Phase 2: Find the start of the cycle
        # Reset slow to head, keep fast at meeting point
        slow = head
        
        while slow != fast:
            slow = slow.next
            fast = fast.next
            
        return slow