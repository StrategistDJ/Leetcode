from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head
        rest = 0
        while curr:
            stack.append(curr)
            curr = curr.next

        while stack:
            popped = stack.pop()
            val = ((popped.val*2)%10) + rest
            rest = (popped.val*2)//10
            popped.val = val
        
        if rest > 0:
            new = ListNode(rest,head)
            head = new
        
        return head

vec = [1, 8, 9]
first = True
for val in vec:
    if first: 
        head = ListNode(val)
        tmp = head
        first = False
    else:
        new = ListNode(val)
        tmp.next = new
        tmp = tmp.next

sol = Solution()
res = sol.doubleIt(head)
while res:
    print(res.val, end = " ")
    res = res.next