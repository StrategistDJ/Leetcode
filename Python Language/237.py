# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#class Solution:
#    def deleteNode(self, node):
#        """
#        :type node: ListNode
#        :rtype: void Do not return anything, modify node in-place instead.
#        """
#        while node.next.next:
#            nxt = node.next
#            node.val = nxt.val
#            node = node.next
#        
#        node.val = node.next.val
#        node.next = None

#Solution 2
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

vec = [4,5,1,9]
find = 5
first = True
for i in vec:
    if first:
        elem = ListNode(i)
        tmp = elem
        first = False
    else:
        new = ListNode(i)
        tmp.next = new
        tmp = tmp.next

l = elem
while elem.val != find:
    elem = elem.next

sol = Solution()
res = sol.deleteNode(elem)
while l:
    print(l.val, end=" ")
    l = l.next