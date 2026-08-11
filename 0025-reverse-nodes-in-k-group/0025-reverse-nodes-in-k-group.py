# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        
        dummy = ListNode(0, head)
        group_prev = dummy
        
        while True:
            # 1. Find the end of the current k-group
            group_end = group_prev
            for _ in range(k):
                group_end = group_end.next
                if not group_end:
                    # Less than k nodes remaining, stop
                    return dummy.next
            
            # 2. Identify the start of the next group before reversing
            group_next = group_end.next
            
            # 3. Reverse the current k-group
            # Standard reverse logic for the segment [group_prev.next ... group_end]
            prev = group_next
            current = group_prev.next
            
            while current != group_next:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            
            # 4. Reconnect the reversed group
            # The old start of the group (now the end) needs to point to group_next
            # The old group_prev needs to point to the new start (which is prev)
            old_group_start = group_prev.next
            group_prev.next = prev
            group_prev = old_group_start