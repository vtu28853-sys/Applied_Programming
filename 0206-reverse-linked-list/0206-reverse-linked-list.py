# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative Approach
        prev = None
        current = head
        
        while current:
            # Store the next node before overwriting the link
            next_node = current.next
            
            # Reverse the link
            current.next = prev
            
            # Move pointers one step forward
            prev = current
            current = next_node
            
        return prev

    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Recursive Approach
        # Base case: if list is empty or has only one node
        if not head or not head.next:
            return head
        
        # Recursively reverse the rest of the