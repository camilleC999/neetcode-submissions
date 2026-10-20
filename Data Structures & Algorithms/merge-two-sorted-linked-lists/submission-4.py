# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = head = ListNode()
        if not list1:
            return list2
        elif not list2:
            return list1

        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        newHead.next = head

        while list1 or list2:
            if not list1:
                head.next = list2
                return newHead.next
            elif not list2:
                head.next = list1
                return newHead.next

            if list1.val <= list2.val:
                head.next = list1
                head = head.next
                list1 = list1.next
            else:
                head.next = list2
                head = head.next
                list2 = list2.next

        return newHead.next

        

        