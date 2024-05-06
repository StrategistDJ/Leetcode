from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        
        prev = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        curr = prev.next
        start = prev
        while curr:
            if prev.val <= curr.val:
                prev.next = curr
                prev = curr
                curr = curr.next
            else:
                curr = curr.next
        prev.next = None

        res = start
        prev = None
        while res:
            tmp = res.next
            res.next = prev
            prev = res
            res = tmp
        
        return prev

vec = [5,2,13,3,8]
first = True
for i in vec:
    if first:
        head = ListNode(i)
        tmp = head
        first = False
    else:
        new = ListNode(i)
        tmp.next = new
        tmp = tmp.next

sol = Solution()
res = sol.removeNodes(head)

while res:
    print(res.val, end=" ")
    res = res.next