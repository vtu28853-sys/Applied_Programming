import heapq
from typing import List, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Min-Heap to store (node_value, index, node)
        # Index is used as a tie-breaker to avoid comparing ListNode objects
        heap = []
        
        # Initialize the heap with the head of each non-empty list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode(0)
        current = dummy
        
        # Counter for tie-breaking if values are equal (optional since we use index)
        # but ensures stability if we were adding new items dynamically without unique IDs
        # The 'i' from the initial loop acts as the unique ID for the list source.
        # When we push a new node from a list, we reuse the original list's index 'i'.
        
        while heap:
            val, idx, node = heapq.heappop(heap)
            
            # Attach the smallest node to the result list
            current.next = node
            current = current.next
            
            # If the popped node has a next node, push it to the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
        
        return dummy.next