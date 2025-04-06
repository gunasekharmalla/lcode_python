# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head is None:
            return 
        fast = slow = head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

Input: head = [3,2,0,-4], pos = 1
Output: true


Input: head = [1,2], pos = 0
Output: true

 Input: head = [1], pos = -1
Output: false       
