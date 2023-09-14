# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node as the head of the merged list
        dummy_head = ListNode()
        current = dummy_head

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        # If there are remaining nodes in list1 or list2, append them to the merged list
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return dummy_head.next
