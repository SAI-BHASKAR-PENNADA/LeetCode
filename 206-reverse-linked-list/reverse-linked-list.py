# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = None
        temp = head
        while temp:
            temp_ = temp.next
            temp.next = ans
            ans = temp
            temp = temp_
        return ans