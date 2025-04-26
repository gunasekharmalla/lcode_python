# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy

        for _ in range(n+1):
            if fast:
                fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return dummy.next

