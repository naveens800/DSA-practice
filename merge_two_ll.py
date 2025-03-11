
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def mergeTwoLists(
            self, list1: Optional[ListNode], list2: Optional[ListNode]
        ) -> Optional[ListNode]:
            dummyNode = ListNode(-1)
            temp = dummyNode
            t1 = list1
            t2 = list2

            
            while t1 and t2:
                if t1.val < t2.val:
                    temp.next = t1
                    temp = t1
                    t1 = t1.next
                else:
                    temp.next = t2
                    temp = t2
                    t2 = t2.next
            if t1:
                temp.next = t1
            else:
                temp.next = t2
            return dummyNode.next
    


