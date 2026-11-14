# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr, prev = slow, None

        while curr:
            saved = curr.next
            curr.next = prev
            prev = curr
            curr = saved

        left, right = head, prev

        while right:
            if left.val == right.val:
                left = left.next
                right = right.next
            else:
                return False
        
        return True
            
        