# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise = hare = head
        while hare:
            tortoise = tortoise.next
            hare = hare.next.next if hare.next else None
            if hare and hare == tortoise:
                return True
        return False
        
