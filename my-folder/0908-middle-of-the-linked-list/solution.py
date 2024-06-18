from typing import Tuple
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        (middle_node, length) = self.get_middle(head, 0, 0)
        return middle_node
        
    def get_middle(self, head: Optional[ListNode], idx: int, length: int) -> Tuple[Optional[ListNode], int]:
        if not head:
            return (None, length)
        
        (new_head, length) = self.get_middle(head.next, idx + 1, length + 1)

        if length % 2 == 0 and idx == length / 2:
            return (head, length)
        elif length % 2 != 0 and idx == length // 2:
            return (head, length)
        else:
            return  (new_head, length)
        


