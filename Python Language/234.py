from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        rev = prev
        slow = head
        while rev:
            if rev.val != slow.val:
                return False
            rev = rev.next
            slow = slow.next
        return True
        
first = True
val = [1,2,3,1]
for i in val:
    if first: 
        link = ListNode(i, None)
        first = False
        tmp = link
    
    else:
        new = ListNode(i)
        tmp.next = new
        tmp = tmp.next

sol = Solution()
res = sol.isPalindrome(link)
print(f"The vector return {res}")