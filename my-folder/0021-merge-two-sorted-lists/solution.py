# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if not list1 or not list2:
            return list1 if list1 else list2

        head = tail = None
        while list1 or list2:
            if not list1 or not list2:
                tail.next = list1 if list1 else list2
                return head
            
            if list1.val < list2.val:
                if not head:
                    head = list1
                    tail = head
                else:
                    tail.next = list1
                    tail = tail.next
                list1 = list1.next
            else:
                if not head:
                    head = list2
                    tail = head
                else:
                    tail.next = list2
                    tail = tail.next
                list2 = list2.next
        return head
        
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
