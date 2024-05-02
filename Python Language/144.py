from typing import List, Optional

#Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recur_visit(self, root, visited)->None:
        if not root:
            return 
        
        visited.append(root.val)
        self.recur_visit(root.left, visited)
        self.recur_visit(root.right, visited)

        return

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return root
        
        output = []
        self.recur_visit(root, output)
        
        return output