# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        ret = ans
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                ans.next = ListNode(list1.val)
                list1 = list1.next
            else:
                ans.next = ListNode(list2.val)
                list2 = list2.next
            ans = ans.next
        
        while list1 != None:
            ans.next = ListNode(list1.val)
            list1 = list1.next
            ans = ans.next
        
        while list2 != None:
            ans.next = ListNode(list2.val)
            list2 = list2.next
            ans = ans.next
        
        return ret.next
