from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#class Solution:
#    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#        n = k-1
#        curr_1 = 0
#        curr_2 = 0
#        count = 0
#        curr = head
#        if not head.next:
#            return head
#Find the first node to swap
#        while curr:
#            if n >= 0:
#                curr_1 = curr
#                n-=1
#            curr = curr.next
#            count+=1
#Find the second one and execute the swap
#        curr = head
#        n = count-k
#        swap = False
#        while curr and not swap:
#            if n >= 0:
#                curr_2 = curr
#                n-=1
#            else:
#                tmp = curr_1.val
#                curr_1.val = curr_2.val
#                curr_2.val = tmp
#                swap = True
#            curr = curr.next
#        if not swap:
#            tmp = curr_1.val
#            curr_1.val = curr_2.val
#            curr_2.val = tmp
#        return head

#Second Solution (faster)
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = head
        second = head
        for i in range(1,k):
            first = first.next
        
        curr = first
        while curr.next:
            second = second.next
            curr = curr.next
        
        tmp = first.val
        first.val = second.val
        second.val = tmp

        return head

nums = [1,2,3,4,5]
val = 2
first = True
for i in nums:
    if first:
        link = ListNode(i)
        tmp = link
        first = False
    else:
        new = ListNode(i)
        tmp.next = new
        tmp = tmp.next

sol = Solution()
res = sol.swapNodes(link, val)

while res:
    print(res.val, end = " ")
    res = res.next