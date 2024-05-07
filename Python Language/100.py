from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rec_check(self, p, q, same)-> bool:
        if not p and same:
            if not q:
                return True
            else:
                return False
        if not q:
            return False     
        if not same or p.val!=q.val:
            return False
        
        same = self.rec_check(p.left, q.left, same)
        same = self.rec_check(p.right,q.right, same)

        return same
        

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.rec_check(p,q,True)

vec_1 = [0, -5]
vec_2 = [0,-8]
first = True
tree1 = TreeNode(vec_1[0])
tree2 = TreeNode(vec_2[0])

tree1.left = TreeNode(vec_1[1])
tree2.left = TreeNode(vec_2[1])

sol = Solution()
res = sol.isSameTree(tree1, tree2)
print(res)