# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = cur = None

        while list1 and list2:
            if list1.val <= list2.val:
                if not merged_list:
                    cur = merged_list = list1
                else:
                    cur.next = list1
                    cur = cur.next
                list1 = list1.next
            else:
                if not merged_list:
                    cur = merged_list = list2
                else:
                    cur.next = list2
                    cur = cur.next
                list2 = list2.next
            
        if list1:
            if not merged_list:
                merged_list = list1
            else:
                cur.next = list1
        
        if list2:
            if not merged_list:
                merged_list = list2
            else:
                cur.next = list2
        
        return merged_list
        
