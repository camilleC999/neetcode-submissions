# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        h1 = list1
        h2 = list2
        nl = None


        if h1.val <= h2.val:
            nl = h1
            h1 = h1.next
        else:
            nl = h2
            h2 = h2.next

        nHead = nl

        while True:
            if h1 is None:
                nl.next = h2
                return nHead
            elif h2 is None:
                nl.next = h1
                return nHead
            
            if (h1.val <= h2.val or h2 is None):
                nl.next = h1
                h1 = h1.next
            elif (h2.val < h1.val or h1 is None):
                nl.next = h2
                h2 = h2.next
            
            if nl.next is not None:
                nl = nl.next

        return nHead

            
                



        

        