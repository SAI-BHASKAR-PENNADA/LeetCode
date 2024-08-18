"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        ans = Node(head.val)

        mapper = {}
        mapper[head] = ans

        tempOrg = head.next 
        tempAns = ans
        
        while tempOrg:
            tempAns.next = Node(tempOrg.val)
            mapper[tempOrg] = tempAns.next
            tempOrg = tempOrg.next
            tempAns = tempAns.next
        
        # print(mapper)
        
        for pointer in mapper.keys():
            if pointer.random:
                mapper[pointer].random = mapper[pointer.random] 
            
        return ans