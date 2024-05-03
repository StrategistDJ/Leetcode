from typing import Optional

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle = head

        while head.next and head.next.next:
            middle = middle.next
            head = head.next.next
        
        if head.next:
            middle = middle.next
            
        return middle

link = ListNode(1, None)
tmp = link
for i in range(2,6):
    new = ListNode(i)
    tmp.next = new
    tmp = tmp.next

sol = Solution()
res = sol.middleNode(link)
while res:
    print(res.val, end="\t")
    res = res.next