# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list, cur = None, head       
        
        while cur:
            nxt = cur.next
            cur.next = new_list
            new_list = cur
            cur = nxt
        
        return new_list



