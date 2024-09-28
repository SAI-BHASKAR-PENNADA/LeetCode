# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        ans = None
        temp = head
        while temp:
            temp_ = temp.next
            temp.next = ans
            ans = temp
            temp = temp_
        return ans

    def reorderList(self, head: Optional[ListNode]) -> None:
        temp = head
        count = 0
        while temp:
            temp = temp.next
            count += 1
        if count <= 2:
            return head
        count = count // 2
        temp = head
        while count > 0:
            count -= 1
            temp = temp.next
        secondhead = temp.next
        temp.next = None
        secondhead = self.reverseList(secondhead)
        # i have head and secondhead head > secondhead
        temphead = head
        tempsecondhead = secondhead
        
        # while temphead:
        #     print(temphead.val)
        #     temphead = temphead.next
        # while tempsecondhead:
        #     print(tempsecondhead.val)
        #     tempsecondhead = tempsecondhead.next

        # temphead = head
        # tempsecondhead = secondhead
        while tempsecondhead:
            temphead_ = temphead.next
            temphead.next = tempsecondhead
            temphead = temphead_

            temphead_ = tempsecondhead.next
            tempsecondhead.next = temphead
            tempsecondhead = temphead_
        return head
