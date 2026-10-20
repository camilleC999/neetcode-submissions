# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = resHead = ListNode()

        while list1 or list2:
            if not list1:
                head.next = list2
                return resHead.next
            elif not list2:
                head.next = list1
                return resHead.next

            if list1.val <= list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next

            head = head.next

        return resHead.next

                



        

        