from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-200)
        temp = head

        l1 = list1
        l2 = list2

        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                temp = temp.next
                l1 = l1.next
            else:
                temp.next = l2
                temp = temp.next
                l2 = l2.next
        
        while l1:
            temp.next = l1
            temp = temp.next
            l1 = l1.next
        
        while l2:
            temp.next = l2
            temp = temp.next
            l2 = l2.next
        return head.next
        
